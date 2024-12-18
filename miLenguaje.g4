grammar miLenguaje;

// Lexer rules
PROGRAMA  : 'programa' ;
FUNCION   : 'funcion' ;
REGRESA   : 'regresa' ;
MUESTRA   : 'muestra' ;
PREGUNTA  : 'pregunta' ;
GUARDA    : 'guarda' ;
EN        : 'en' ;
CREA      : 'crea' ;
ARREGLO   : 'arreglo' ;
MATRIZ    : 'matriz' ;
SI        : 'si' ;
SINO      : 'sino' ;
MIENTRAS  : 'mientras' ;
PARA      : 'para' ;

// Tipos de datos
NUMERO    : 'numero' ;
DECIMAL   : 'decimal' ;
TEXTO     : 'texto' ;
LOGICO    : 'logico' ;

// Operadores
SUMA      : '+' ;
RESTA     : '-' ;
MULTIPLICA: '×' ;
DIVIDE    : '÷' ;
POTENCIA  : '^' ;
RAIZ      : '√' ;

// Comparadores y lógicos
IGUAL     : '=' ;
NO_IGUAL  : '≠' ;
MAYOR     : '>' ;
MENOR     : '<' ;
MAYOR_IGUAL: '>=' ;
MENOR_IGUAL: '<=' ;
Y         : 'y' ;
O         : 'o' ;
NO        : 'no' ;

// Tipos de valores
BOOLEANO  : 'verdadero' | 'falso' ;
NUMERO_VAL: '-'? [0-9]+ ;
DECIMAL_VAL: '-'? [0-9]+ '.' [0-9]+ ;
TEXTO_VAL : '"' (~["])* '"' ;
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]* ;

// Símbolos
LPAREN    : '(' ;
RPAREN    : ')' ;
LBRACE    : '{' ;
RBRACE    : '}' ;
LBRACKET  : '[' ;
RBRACKET  : ']' ;
PUNTO_COMA: ';';
COMA      : ',' ;

// Espacios en blanco y comentarios
WS        : [ \t\r\n]+ -> skip ;
COMENTARIO: '//' ~[\r\n]* -> skip ;

// Regla principal
programa: PROGRAMA LBRACE declaracion* sentencia* RBRACE EOF;

// Declaraciones
declaracion: declaracion_funcion
           | declaracion_variable
           ;

// Declaración de función
declaracion_funcion: FUNCION IDENTIFICADOR LPAREN parametros? RPAREN LBRACE 
                     sentencia* 
                     regresar? 
                   RBRACE ;

// Parámetros de función
parametros: (NUMERO | DECIMAL | TEXTO | LOGICO) IDENTIFICADOR (COMA (NUMERO | DECIMAL | TEXTO | LOGICO) IDENTIFICADOR)* ;

// Sentencias
sentencia: declaracion_variable
         | asignacion
         | entrada
         | salida
         | condicional
         | bucle
         | llamada_funcion
         | regresar
         ;

// Declaración de variable
declaracion_variable: CREA (ARREGLO | MATRIZ)? 
                      (NUMERO | DECIMAL | TEXTO | LOGICO) 
                      IDENTIFICADOR (IGUAL expresion)? PUNTO_COMA ;

// Asignación
asignacion: IDENTIFICADOR (LBRACKET expresion RBRACKET)* IGUAL expresion PUNTO_COMA ;

// Entrada
entrada: PREGUNTA TEXTO_VAL GUARDA (NUMERO | DECIMAL | TEXTO | BOOLEANO) EN IDENTIFICADOR PUNTO_COMA ;

// Salida
salida: MUESTRA expresion PUNTO_COMA ;

//Regresar
regresar: REGRESA expresion PUNTO_COMA ;

// Condicional
condicional: condicional_si condicional_sino*;

// Condicional_si
condicional_si: SI LPAREN condicion RPAREN LBRACE sentencia* RBRACE ;

// Condicional_sino
condicional_sino: SINO (SI LPAREN condicion RPAREN)? LBRACE sentencia* RBRACE? ;

// Bucles
bucle: bucle_mientras | bucle_para ;

bucle_mientras: MIENTRAS LPAREN condicion RPAREN LBRACE sentencia* RBRACE ;

bucle_para: PARA LPAREN CREA (NUMERO | DECIMAL | TEXTO | LOGICO) IDENTIFICADOR IGUAL NUMERO_VAL PUNTO_COMA condicion PUNTO_COMA incremento RPAREN 
            LBRACE sentencia* RBRACE ;

// Incremento
incremento: IDENTIFICADOR IGUAL IDENTIFICADOR (SUMA | RESTA) NUMERO_VAL ;

condicion: (LPAREN condicion RPAREN) 
          | expresion (IGUAL | NO_IGUAL | MAYOR | MENOR | MAYOR_IGUAL | MENOR_IGUAL) expresion
          | condicion (Y | O) condicion
          | NO condicion
          | llamada_funcion
          | IDENTIFICADOR
          ;


// Expresión
expresion
    : LPAREN expresion RPAREN //parentesis
    | RAIZ LPAREN expresion RPAREN //raiz
    | expresion POTENCIA expresion  //potencia
    | expresion (SUMA | RESTA | MULTIPLICA | DIVIDE) expresion //operacion basica
    | NUMERO_VAL //numero
    | DECIMAL_VAL //numero decimal
    | TEXTO_VAL //texto
    | BOOLEANO //booleano
    | IDENTIFICADOR //nombre de variable
    | llamada_funcion //llamada de funcion
    | LBRACKET expresion (COMA expresion)* RBRACKET (COMA LBRACKET expresion (COMA expresion)* RBRACKET)*//Arreglo y matriz
    | IDENTIFICADOR LBRACKET expresion RBRACKET (RBRACKET LBRACKET expresion RBRACKET)? //acceso a arreglo o matriz

    ;


// Llamada a función
llamada_funcion: IDENTIFICADOR LPAREN (expresion (COMA expresion)*)? RPAREN ;