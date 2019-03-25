# Importo el archivo indicando la carpeta y el nombre sin la extensión, si no estuviera en una carpeta podría omitir "from carpeta"
from carpeta import archivo
a=1
b=2
# Llamo al archivo y la funcion con el formato "archivo.funcion()"
# Tengo que enviar los datos que necesita el archivo, por eso incluyo (a,b)
archivo.sumar(a,b)
# Llamo a la variable con archivo.variable
print(archivo.resultado)
print('Archivo raíz')
"""En resumen puedo usar cualquier funcion o variable de otro archivo simplemente importandolo y 
colocando el nombre del archivo seguido de un punto y la variable/funcion que quiero ejecutar"""