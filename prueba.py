import os

os.system('echo off')
os.system('cls')

def inicio():
  os.system('cls')

  try:
    global bebidas
    global seleccion
    print('1. Coca-Cola \n2. Fanta de limón \n3. Fanta de naranja')
    bebidas={'1': 1.80,'2': 1.50,'3': 1.60 }
    seleccion= input('Numero de la bebida: ')
    os.system('cls')
    pago()
      
  except:
    inicio()

def pago():

  try:
    cobro= float(input(f'Insete {bebidas[seleccion]}€'))
    while cobro < bebidas[seleccion]:
      print(f'Has introducido un total de {cobro}€, falta {cobro - bebidas[seleccion]}')
      cobro= cobro + float(input('Añadir'))
      total=cobro-bebidas[seleccion]
          
  except:
    print ('Moneda no valida')
    pago()
  final= round(float(cobro - bebidas[seleccion]),2)
  print (f'Le sobra {final}€')


inicio()
