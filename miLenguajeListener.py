# Generated from miLenguaje.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miLenguajeParser import miLenguajeParser
else:
    from miLenguajeParser import miLenguajeParser

# This class defines a complete listener for a parse tree produced by miLenguajeParser.
class miLenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by miLenguajeParser#programa.
    def enterPrograma(self, ctx:miLenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#programa.
    def exitPrograma(self, ctx:miLenguajeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:miLenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:miLenguajeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:miLenguajeParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:miLenguajeParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#parametros.
    def enterParametros(self, ctx:miLenguajeParser.ParametrosContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#parametros.
    def exitParametros(self, ctx:miLenguajeParser.ParametrosContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#sentencia.
    def enterSentencia(self, ctx:miLenguajeParser.SentenciaContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#sentencia.
    def exitSentencia(self, ctx:miLenguajeParser.SentenciaContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:miLenguajeParser.Declaracion_variableContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:miLenguajeParser.Declaracion_variableContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#asignacion.
    def enterAsignacion(self, ctx:miLenguajeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#asignacion.
    def exitAsignacion(self, ctx:miLenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#entrada.
    def enterEntrada(self, ctx:miLenguajeParser.EntradaContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#entrada.
    def exitEntrada(self, ctx:miLenguajeParser.EntradaContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#salida.
    def enterSalida(self, ctx:miLenguajeParser.SalidaContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#salida.
    def exitSalida(self, ctx:miLenguajeParser.SalidaContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#regresar.
    def enterRegresar(self, ctx:miLenguajeParser.RegresarContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#regresar.
    def exitRegresar(self, ctx:miLenguajeParser.RegresarContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#condicional.
    def enterCondicional(self, ctx:miLenguajeParser.CondicionalContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#condicional.
    def exitCondicional(self, ctx:miLenguajeParser.CondicionalContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#condicional_si.
    def enterCondicional_si(self, ctx:miLenguajeParser.Condicional_siContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#condicional_si.
    def exitCondicional_si(self, ctx:miLenguajeParser.Condicional_siContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#condicional_sino.
    def enterCondicional_sino(self, ctx:miLenguajeParser.Condicional_sinoContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#condicional_sino.
    def exitCondicional_sino(self, ctx:miLenguajeParser.Condicional_sinoContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#bucle.
    def enterBucle(self, ctx:miLenguajeParser.BucleContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#bucle.
    def exitBucle(self, ctx:miLenguajeParser.BucleContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#bucle_mientras.
    def enterBucle_mientras(self, ctx:miLenguajeParser.Bucle_mientrasContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#bucle_mientras.
    def exitBucle_mientras(self, ctx:miLenguajeParser.Bucle_mientrasContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#bucle_para.
    def enterBucle_para(self, ctx:miLenguajeParser.Bucle_paraContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#bucle_para.
    def exitBucle_para(self, ctx:miLenguajeParser.Bucle_paraContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#incremento.
    def enterIncremento(self, ctx:miLenguajeParser.IncrementoContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#incremento.
    def exitIncremento(self, ctx:miLenguajeParser.IncrementoContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#condicion.
    def enterCondicion(self, ctx:miLenguajeParser.CondicionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#condicion.
    def exitCondicion(self, ctx:miLenguajeParser.CondicionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#expresion.
    def enterExpresion(self, ctx:miLenguajeParser.ExpresionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#expresion.
    def exitExpresion(self, ctx:miLenguajeParser.ExpresionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:miLenguajeParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:miLenguajeParser.Llamada_funcionContext):
        pass



del miLenguajeParser