from miLenguajeListener import miLenguajeListener;
from miLenguajeParser import miLenguajeParser;

class traduceToPython(miLenguajeListener):
    def __init__(self): 
        self.code = ""
        self.nTab = 0
        
    def constTab(self):
        return self.nTab * '\t'
    
    #función para importar una librería
    def importar_lib(self, lib):        
        if f"import {lib}" not in self.code:
            salto = '\n\n' if 'import' not in self.code else ''
            self.code = f"import {lib}{salto}" + self.code

    
    #Funcion para procesar una condición
    def procesar_condicion(self, ctx):
        if len(ctx.expresion()) == 2:  # Es una comparación
            exp1 = self.procesar_expresion(ctx.expresion(0))
            exp2 = self.procesar_expresion(ctx.expresion(1))
            
            if ctx.IGUAL():
                return f"{exp1} == {exp2}"
            elif ctx.NO_IGUAL():
                return f"{exp1} != {exp2}"
            elif ctx.MAYOR():
                return f"{exp1} > {exp2}"
            elif ctx.MENOR():
                return f"{exp1} < {exp2}"
            elif ctx.MAYOR_IGUAL():
                return f"{exp1} >= {exp2}"
            elif ctx.MENOR_IGUAL():
                return f"{exp1} <= {exp2}"
                
        elif ctx.Y() or ctx.O():  # Es una operación AND o OR
            op = "and" if ctx.Y() else 'or'
            cond1 = self.procesar_condicion(ctx.condicion(0))
            cond2 = self.procesar_condicion(ctx.condicion(1))
            return f"{cond1} {op} {cond2}"
            
        elif ctx.NO():  # Es una negación
            return f"not {self.procesar_condicion(ctx.condicion(0))}"
        
        elif ctx.llamada_funcion():
            expresiones = []
            for exp in ctx.llamada_funcion().expresion():
                expresiones.append(self.procesar_expresion(exp))
            return f'{ctx.llamada_funcion().IDENTIFICADOR().getText()}({", ".join(expresiones)})'
        
        elif ctx.IDENTIFICADOR():
            ctx.IDENTIFICADOR().getText()
        
        elif ctx.LPAREN() and ctx.RPAREN():
            return f"{self.procesar_condicion(ctx.condicion(0))}"
        
        return ctx.getText()
    
    #funcion para procesar una expresión
    def procesar_expresion(self, ctx):
        if ctx.RAIZ():
            self.importar_lib('math')
            return f"math.sqrt({self.procesar_expresion(ctx.expresion(0))})"
        
        elif ctx.LPAREN() and ctx.RPAREN():
            return f"({self.procesar_expresion(ctx.expresion())})"
        
        elif ctx.POTENCIA():
            self.importar_lib('math')
            return f"math.pow({self.procesar_expresion(ctx.expresion(0))}, {self.procesar_expresion(ctx.expresion(1))})"
        
        elif ctx.SUMA() or ctx.RESTA() or ctx.MULTIPLICA() or ctx.DIVIDE():
            op = ''
            if ctx.SUMA():
                op = '+'
            elif ctx.RESTA():
                op = '-'
            elif ctx.MULTIPLICA():
                op = '*'
            elif ctx.DIVIDE(): 
                op = '/'
            return f"{self.procesar_expresion(ctx.expresion(0))} {op} {self.procesar_expresion(ctx.expresion(1))}"
        
        elif ctx.LBRACKET() and ctx.RBRACKET() and ctx.IDENTIFICADOR():
            return f"{ctx.IDENTIFICADOR()}[{self.procesar_expresion(ctx.expresion(0))}]"
               
        elif ctx.NUMERO_VAL() or ctx.DECIMAL_VAL() or ctx.TEXTO_VAL() or ctx.IDENTIFICADOR():
            if ctx.NUMERO_VAL():
                return ctx.NUMERO_VAL().getText()
            elif ctx.DECIMAL_VAL():
                return ctx.DECIMAL_VAL().getText()
            elif ctx.TEXTO_VAL():
                return ctx.TEXTO_VAL().getText()
            else:
                return ctx.IDENTIFICADOR().getText()
        
        elif ctx.BOOLEANO():
            return 'True' if ctx.BOOLEANO().getText() == 'verdadero' else 'False'
        
        elif ctx.llamada_funcion():
            expresiones = []
            for exp in ctx.llamada_funcion().expresion():
                expresiones.append(self.procesar_expresion(exp))
            return f'{ctx.llamada_funcion().IDENTIFICADOR().getText()}({", ".join(expresiones)})'

        elif ctx.LBRACKET() and ctx.RBRACKET():
            # Lista para almacenar todas las expresiones y sus posiciones
            tokens = []
            
            # Recorremos todos los tokens hijos del contexto
            for i in range(len(ctx.children)):
                child = ctx.children[i]
                if child.getText() == '[' or child.getText() == ']' or child.getText() == ',':
                    tokens.append(child.getText())
                else:
                    tokens.append(self.procesar_expresion(child))

            # Procesamos los tokens para construir la matriz
            result = []
            current_array = []

            for token in tokens:
                if token == '[':
                    current_array = []
                elif token == ']':
                    result.append(f"[{', '.join(current_array)}]")
                elif token == ',':
                    continue  # Ignoramos las comas entre subarreglos
                else:  #se encontro un valor del arreglo
                    current_array.append(str(token))
            if(len(result) > 1):
                return f"[{', '.join(result)}]"
            else:
                return result[0]
        
        else:
            return ''
        
    #función para convertir una concatenacion a fstring
    def convertir_a_fstring(self,texto):
        
        if len(texto.split('+')) > 1:
            # Separar por los símbolos de concatenación ('+')
            partes = texto.split('+')
        
            # Limpiar espacios en blanco
            partes = [p.strip() for p in partes]
            
            
            # Identificar las variables (las partes que no están entre comillas)
            resultado = ''
            for parte in partes:
                if parte.strip('"').strip("'") == parte:  # Es una variable
                    resultado += '{' + parte.strip() + '}'
                else:  # Es texto literal
                    resultado += parte.strip('"').strip("'")
                    
            return 'f"' + resultado + '"'
        else:
            return texto
        
    # Enter a parse tree produced by miLenguajeParser#programa.
    def enterPrograma(self, ctx:miLenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#programa.
    def exitPrograma(self, ctx:miLenguajeParser.ProgramaContext):
        # Especificamos el nombre del archivo y abrimos en modo de escritura
        file_name = "programaTraducido.py"
        with open(file_name, "w") as file:
            file.write(self.code)

        print(f"El código ha sido guardado en el archivo '{file_name}'.")

    # Enter a parse tree produced by miLenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:miLenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:miLenguajeParser.DeclaracionContext):
        pass


    def enterDeclaracion_funcion(self, ctx:miLenguajeParser.Declaracion_funcionContext):
        # Obtener el nombre de la función
        nombre_funcion = ctx.IDENTIFICADOR().getText()
        
        # Obtener los parámetros si existen
        parametros = ", ".join(param.getText() for param in ctx.parametros().IDENTIFICADOR()) if ctx.parametros() else ""

        # Construir la definición de la función
        self.code += f'def {nombre_funcion}({parametros}):\n'
        
        #Aumentar en uno el tabulador
        self.nTab += 1

    # Exit a parse tree produced by miLenguajeParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:miLenguajeParser.Declaracion_funcionContext):
            
        #Disminuir el tabulado
        self.nTab -= 1
        
        self.code += "\n"


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
        #Se obtiene el nombre de la variable
        nombre_variable = ctx.IDENTIFICADOR().getText()
        
        valor = ""

        #Obtener el valor de la variable si existe
        if ctx.expresion():
            
            valor = f"{self.convertir_a_fstring(self.procesar_expresion(ctx.expresion()))}"
        elif ctx.NUMERO():
            valor = 0
        elif ctx.DECIMAL():
            valor = 0.0
        elif ctx.TEXTO():
            valor = "\"\""
        else:
            valor = False
        
        self.code += f"\n{self.constTab()}{nombre_variable} = {valor}"

    # Exit a parse tree produced by miLenguajeParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:miLenguajeParser.Declaracion_variableContext):
        self.code += "\n"


    # Enter a parse tree produced by miLenguajeParser#asignacion.
    def enterAsignacion(self, ctx:miLenguajeParser.AsignacionContext):
        #Se obtiene el nombre de la variable
        nombre_variable = ctx.IDENTIFICADOR().getText()
        acceso = ''
        if ctx.LBRACKET() and ctx.RBRACKET():
            # Recorremos todos los tokens hijos del contexto
            for i in range(len(ctx.expresion())-1):
                acceso += f"[{self.procesar_expresion(ctx.expresion(i))}]"
            valor = self.procesar_expresion(ctx.expresion(len(ctx.expresion())-1))
        else:
            valor = self.procesar_expresion(ctx.expresion(0))        
        
        #se guarda la instrucción
        self.code += f"\n{self.constTab()}{nombre_variable}{acceso} = {valor}"

    # Exit a parse tree produced by miLenguajeParser#asignacion.
    def exitAsignacion(self, ctx:miLenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#entrada.
    def enterEntrada(self, ctx:miLenguajeParser.EntradaContext):
        #Se obtiene el nombre de la variable
        nombre_variable = ctx.IDENTIFICADOR().getText()
        
        #Se obtiene el tipo de valor de entrada
        tipo = ""
        if ctx.NUMERO():
            tipo = 'int'
        elif ctx.DECIMAL():
            tipo = 'float'
        elif ctx.BOOLEANO():
            tipo = 'bool'
        else:
            tipo = 'str'
        
        #se obtiene el texto a mostrar        
        txt = ctx.TEXTO_VAL().getText()
        
        #se guarda la instrucción
        self.code += f"\n{self.constTab()}{nombre_variable} = {tipo}(input({txt}))"
        

    # Exit a parse tree produced by miLenguajeParser#entrada.
    def exitEntrada(self, ctx:miLenguajeParser.EntradaContext):
        self.code += "\n"


    # Enter a parse tree produced by miLenguajeParser#salida.
    def enterSalida(self, ctx:miLenguajeParser.SalidaContext):
        
        valor = self.convertir_a_fstring(self.procesar_expresion(ctx.expresion()))
        
        self.code += f"\n{self.constTab()}print({valor})"

    # Exit a parse tree produced by miLenguajeParser#salida.
    def exitSalida(self, ctx:miLenguajeParser.SalidaContext):
        self.code += "\n"

    # Enter a parse tree produced by miLenguajeParser#regresar.
    def enterRegresar(self, ctx:miLenguajeParser.RegresarContext):
        valor = ''
        
        valor = self.procesar_expresion(ctx.expresion())
        
        self.code += f"\n{self.constTab()}return {valor}"

    # Exit a parse tree produced by miLenguajeParser#regresar.
    def exitRegresar(self, ctx:miLenguajeParser.RegresarContext):
        pass

    # Enter a parse tree produced by miLenguajeParser#condicional.
    def enterCondicional(self, ctx:miLenguajeParser.CondicionalContext):
        pass
        
    # Exit a parse tree produced by miLenguajeParser#condicional.
    def exitCondicional(self, ctx:miLenguajeParser.CondicionalContext):
        self.code += '\n'

    # Enter a parse tree produced by miLenguajeParser#condicional_si.
    def enterCondicional_si(self, ctx:miLenguajeParser.Condicional_siContext):
        #obtener la condición
        condicion = self.procesar_condicion(ctx.condicion())
        
        #guardar la intrucción
        self.code += f"\n{self.constTab()}if {condicion}:\n"
        
        #Aumentar tabulador
        self.nTab += 1
                
    # Exit a parse tree produced by miLenguajeParser#condicional_si.
    def exitCondicional_si(self, ctx:miLenguajeParser.Condicional_siContext):        
        #Diminuir tabulador
        self.nTab -= 1


    # Enter a parse tree produced by miLenguajeParser#condicional_sino.
    def enterCondicional_sino(self, ctx:miLenguajeParser.Condicional_sinoContext):
        if ctx.condicion():  # es un 'sino si'
            #ontener la condición
            condicion = self.procesar_condicion(ctx.condicion())
            
            #guardar instrución
            self.code += f"\nelif {condicion}:\n"
            
        else:  # es un 'sino'
            #guardar instrucción
            self.code +="\n" + self.constTab() + "else:\n"
            
        #Aumentar tabulador
        self.nTab += 1

    # Exit a parse tree produced by miLenguajeParser#condicional_sino.
    def exitCondicional_sino(self, ctx:miLenguajeParser.Condicional_sinoContext):
        #Diminuir tabulador
        self.nTab -= 1


    # Enter a parse tree produced by miLenguajeParser#bucle.
    def enterBucle(self, ctx:miLenguajeParser.BucleContext):
        pass

    # Exit a parse tree produced by miLenguajeParser#bucle.
    def exitBucle(self, ctx:miLenguajeParser.BucleContext):
        pass


    # Enter a parse tree produced by miLenguajeParser#bucle_mientras.
    def enterBucle_mientras(self, ctx:miLenguajeParser.Bucle_mientrasContext):
        #obtener la condición
        condicion = self.procesar_condicion(ctx.condicion())
        
        #guardar la intrucción
        self.code += f"\n{self.constTab()}while {condicion}:\n"
        
        #Aumentar tabulador
        self.nTab += 1

    # Exit a parse tree produced by miLenguajeParser#bucle_mientras.
    def exitBucle_mientras(self, ctx:miLenguajeParser.Bucle_mientrasContext):
        #Diminuir tabulador
        self.nTab -= 1
        
        self.code += "\n"

    # Enter a parse tree produced by miLenguajeParser#bucle_para.
    def enterBucle_para(self, ctx:miLenguajeParser.Bucle_paraContext):
        'PARA LPAREN declaracion_variable condicion PUNTO_COMA incremento RPAREN '
        #se obtiene la variable
        declaracion_variable = ctx.IDENTIFICADOR().getText()
        
        #Obtener el inicio del ciclo
        if(ctx.NUMERO_VAL().getText() != '0'):
            inicio = f"{ctx.NUMERO_VAL().getText()}, "
        else:
            inicio = ''
        
        #obtener el final
        final = self.procesar_expresion(ctx.condicion().expresion(1))
        
        #obtener el salto
        if(ctx.incremento().NUMERO_VAL().getText() != '1'):
            if(ctx.incremento().RESTA()):
                salto = f", -{ctx.incremento().NUMERO_VAL()}"
            else:
                salto = f", {ctx.incremento().NUMERO_VAL()}"
        else:
            salto = ''
        
        
        #guardar la instrucción
        self.code += f"\n{self.constTab()}for {declaracion_variable} in range({inicio}{final}{salto}):\n"
        
        #Aumentar tabulador
        self.nTab += 1

    # Exit a parse tree produced by miLenguajeParser#bucle_para.
    def exitBucle_para(self, ctx:miLenguajeParser.Bucle_paraContext):
        #Diminuir tabulador
        self.nTab -= 1
        
        self.code += "\n"


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