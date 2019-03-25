"""He provocado un error intentando imprimir una variable no declarada, para evitar el cierre del programa he usado "try" (intenta), en caso de que la ejecución sea correcta seguirá y no ejecutará el except, en el momento en que falle parará el bloque try y pasará al except"""
try:
    print('1- Hello World')
except:
    print('Error')
try:
    print('2- Buscando variable1')
    print(variable1)
except:
    print("3- No se encuentra la variable1")