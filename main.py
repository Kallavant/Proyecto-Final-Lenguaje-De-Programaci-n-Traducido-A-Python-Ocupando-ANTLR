from  antlr4 import *
from miLenguajeLexer import miLenguajeLexer
from miLenguajeParser import miLenguajeParser
from miLenguajeListener import miLenguajeListener
from traduceToPython import traduceToPython

def main():
    in_code = input('File name> ')
    fileopen = open(in_code)
    
    lexer = miLenguajeLexer(InputStream(fileopen.read()))
    stream = CommonTokenStream(lexer)
    parser = miLenguajeParser(stream)
    tree = parser.programa()
    
    #print(tree.toStringTree(recog=parser))
    walter = ParseTreeWalker()
    walter.walk(traduceToPython(),tree)
    
if __name__=='__main__':
    main()