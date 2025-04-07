def firstUniqChar(palavra):
    i = 0
    while(i<len(palavra)):
      count = 0
      for letra in palavra:
        if(palavra[i] == letra):
          count+=1
      if(count == 1):
        answer = palavra[i]
        i = len(palavra) - 1
      elif(count > 1 and i == len(palavra) - 1):
        answer = '-1'
      i+=1
    return answer

palavra = 'abacabad'
print(firstUniqChar(palavra))
palavra = 'aaabb'
print(firstUniqChar(palavra))