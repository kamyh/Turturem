import ply.yacc as yacc

from lex_ import tokens
import AST

def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    ''' programme : statement '<' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : expression
        | structure'''
    p[0] = p[1]

def p_expression_motif(p):
    ''' expression : MOTIF '.' VALUE '.' COLOR '''
    p[0] = AST.OpNode(AST.TokenNode(p[2]),[AST.TokenNode(p[1]),AST.TokenNode(p[3]),AST.TokenNode(p[5])])

def p_value(p):
    '''VALUE : NUMBER
        | GRADUS_ '''
    p[0] = p[1]

def p_gradus(p):
    '''GRADUS_ : GRADUS ':' NUMBER'''
    p[0] = "%s%s%d"%(p[1],p[2],p[3])

def p_structure(p):
    ''' structure : QUIA '.' NUMBER '.' NUMBER '.' NUMBER '<' programme FINIS '''
    p[0] = AST.WhileNode([AST.TokenNode(p[3]),AST.TokenNode(p[5]),AST.TokenNode(p[7]),p[9]])
   # p[0] = AST.TokenNode(p[1])#AST.forNode([p[2],p[4]])


def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Syntax error: unexpected end of file!")

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys 
    	
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)

    if result:
        print (result)
            
        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name)
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")
