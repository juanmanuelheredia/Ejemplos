import datetime
def saludar():
  print('Hola')
  print(datetime.datetime.now())

def despedirse():
  print('Adios')

menu=int(input('Escribe 1 o 2 '))
if menu==1:
  saludar()
elif menu==2:
  despedirse()



