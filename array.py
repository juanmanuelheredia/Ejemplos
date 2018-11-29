# Crear el array
array=['hola','mundo']
# Imprimir n array
print(array[0])
print(array[1])
# Añadir valor a array
array.append('adios')
array.append('mundo')
# Calcular longitud array
print(f' El array tiene {len(array)} valores')
print(f'Que son {array}')
# Imprimir desde el 0 hasta :n
n=2
print(f'Los {n} primeros valores son {array[:n]}')
array.remove('mundo')
print(array)