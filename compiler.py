import AST
from AST import addToClass

#have to do that way because os 120 character len limitation
tForwardSize = 't.forward(size)'

compteurIncrementation = -1
espaceTablulation = ""


shapes = {
    'triangulum': ['t.forward(size)','t.left(120)','t.forward(size)','t.left(120)','t.forward(size)'],
    'quadratum': [tForwardSize,'t.right(90)',tForwardSize,'t.right(90)',tForwardSize,'t.right(90)',tForwardSize,'t.right(90)'],
    'circulus': ['t.circle(size)']
}

others = {
    'circumactio': ['t.right(size)']
}

colors = {
    'caeruleum': 'BLUE',
    'rufus': 'RED',
    'viridis': 'GREEN',
    'nigrum': 'BLACK'
}



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
            tab = shapes[self.tok]
            i=0
            while i<len(tab):
                bytecode += "%s%s\n" %(espaceTablulation,tab[i])
                i+=1
        else:
            if self.tok in colors:
                bytecode += "t.pencolor(\"%s\")\n" % colors[self.tok]
            elif 'gradus' in self.tok:
                tampon = self.tok.split(":");
                bytecode += "%ssize=i%s\n" %(espaceTablulation,tampon[1])
            elif self.tok in others:
                tab = others[self.tok]
                i=0
                while i<len(tab):
                    bytecode += "%s%s\n" %(espaceTablulation,tab[i])
                    i+=1

            else:
                bytecode += "%s%s\n" %(espaceTablulation,self.tok)
    else:
        bytecode += "%ssize=%s\n" %(espaceTablulation,self.tok)
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

    global compteurIncrementation
    compteurIncrementation +=1

    bytecode += "%sfor i%s in range(%s,%s,%s) :\n" %(espaceTablulation,compteurIncrementation.trim(),self.children[2].trim(), self.children[0].trim(),self.children[1].trim())

    global espaceTablulation

    espaceTablulation = "";
    for a in range(0,compteurIncrementation+1):
        espaceTablulation+="\t";

    bytecode += "%s%s\n" %(espaceTablulation,self.children[3].compile())

    compteurIncrementation -=1

    espaceTablulation = "";
    for a in range(0,compteurIncrementation+1):
        espaceTablulation+="\t";


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