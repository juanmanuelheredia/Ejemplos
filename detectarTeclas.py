import sys
 
x='si'
 
while x=='si':
    tecla = sys.stdin.read(1)
    print (f'Has presionado {tecla}')
    if tecla=='s':
        x='no'