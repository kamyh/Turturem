import AST
from AST import addToClass

#have to do that way because os 120 character len limitation
tForwardSize = 't.forward(size)'



shapes = {
    'triangulum': 't.forward(size)\nt.left(120)\nt.forward(size)\nt.left(120)\nt.forward(size)',
    'quadratum': tForwardSize+'\nt.right(90)\n'+tForwardSize+'\nt.right(90)\n'+tForwardSize+'\nt.right(90)\n'+tForwardSize+'\nt.right(size)',
    'circulus': 't.circle(size)'
}

colors = {
    'caeruleum': 'BLUE',
    'rufus': 'RED',
    'viridis': 'GREEN',
    'nigrum': 'BLACK'
}

global_gradus = []

def whilecounter():
    whilecounter.current += 1
    return whilecounter.current
whilecounter.current = 0


@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()
    bytecode += ""
    return bytecode


@addToClass(AST.TokenNode)
def compile(self):
    bytecode = ""
    if isinstance(self.tok, str):
        print(self.tok)
        if self.tok in shapes:
            bytecode += "%s\n" % shapes[self.tok]
        else:
            if self.tok in colors:
                bytecode += "t.pencolor(\"%s\")\n" % colors[self.tok]
            else:
                if 'gradus' in self.tok:
                    bytecode += "size=%s\n" % self.tok
                else:
                    bytecode += "%s\n" % self.tok
    else:
        bytecode += "size=%s\n" % self.tok
    return bytecode


@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    if len(self.children) == 1:
        bytecode += self.children[0].compile()
        bytecode += "USUB\n"
    else:
        for c in self.children:
            bytecode += c.compile()
        #bytecode += self.op + "\n"
    return bytecode

@addToClass(AST.ForNode)
def compile(self):
    bytecode = ""
    print(self.type)
    global_gradus.append(self)
    bytecode += "%s\n" % self.rest.compile()
    return bytecode


if __name__ == "__main__":
    #connot call a file "parser.py" !
    from parser_ import parse
    import sys
    import os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = "import turtle\nt=turtle.Turtle()\nt.speed(1)\nt.shape('turtle')\n"
    compiled += ast.compile()
    compiled += "wn = turtle.Screen()\nwn.exitonclick()"
    name = os.path.splitext(sys.argv[1])[0]+'.py'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print ("Wrote output to", name)