comentarios = 'blue,red,green'
comentarios.split(",")
array1 = 'hola','hasta,hey'
array2 = 'buenas','luego,oye'
# registros=str.len(array1)
diccionario={}
# for array1 in registros:
n=0
for comentarios in array1:
  
  diccionario.update({array1[n]:array2[n]})
  print(diccionario)
  # print(comentarios[1])
  n=n+1