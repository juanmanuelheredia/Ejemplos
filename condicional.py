print('Vamos a comparar 4 valores de 2 en 2')
condicion1=input('Escribe algo')
igual1=input('Dime algo más para compararlo')
condicion2=input('Escribe algo')
igual2=input('Dime algo más para compararlo')
if condicion1 == igual1 and condicion2 == igual2:
  print('Ambas comparaciones son correctas')
  print(condicion1, igual1, condicion2, igual2)
elif condicion1 == igual1 or condicion2 == igual2:
  print('Una de las comparaciones es correcta')
  if condicion1 == igual1:
    print('La condicion 1 es igual a la comparación 1')
  elif condicion2 == igual2:
    print('La condicion 2 es igual a la comparación 2')
else:
  print('Ninguna de las comparaciones es igual')