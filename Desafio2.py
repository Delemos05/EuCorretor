def merge_intervals(lista):
    i=0
    while(i<len(lista)):
      if(lista[i][i]<lista[i+1][i]):
        inicio = lista[i][i]
        if(lista[i][i+1]<lista[i+1][i+1]):
          fim = lista[i+1][i+1]
          [lista[i][i], lista[i][i+1]]=[inicio, fim]
          lista.remove([lista[i+1][i], lista[i+1][i+1]])
          i = len(lista)-1
      i+=1
    return lista
lista = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals(lista))
lista = [[1,4], [4,5]]
print(merge_intervals(lista))