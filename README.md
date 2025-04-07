# EuCorretor
Resolvendo os desafios da EuCorretorImoveis


Exercício 1: Encontrar o Primeiro Caractere Não Repetido em uma String

- Descrição: Neste exercício, você deve implementar uma função que encontra o primeiro caractere que não se repete em uma string. Caso todos os caracteres sejam repetidos, a função deve retornar -1.
 
Exemplo:
firstUniqChar("abacabad")  # Saída: 3 ('c')
firstUniqChar("aaabb")      # Saída: -1 (não há caracteres não repetidos)

Exercício 2: Mesclar Intervalos

- Descrição: Dada uma lista de intervalos, você deve implementar uma função que mescla os intervalos sobrepostos. Cada intervalo é representado por um par de números [início, fim]. Caso dois intervalos se sobreponham, eles devem ser combinados em um único intervalo.

Exemplo:
merge_intervals([[1,3], [2,6], [8,10], [15,18]])  
# Saída: [[1, 6], [8, 10], [15, 18]]

merge_intervals([[1,4], [4,5]])  
# Saída: [[1, 5]]

Exercício 3: Word Ladder (Escada de Palavras)

- Descrição: Neste exercício, você deve implementar uma função que encontra o comprimento do caminho mais curto de transformação de uma palavra inicial para uma palavra final, seguindo as regras abaixo:
  1. A cada transformação, apenas uma letra pode ser alterada.
  2. Cada palavra intermediária deve existir no dicionário fornecido.
 
  A entrada do exercício será composta por duas palavras de mesma dimensão e uma lista de palavras. Sua tarefa é encontrar a sequência mais curta de transformações, ou retornar 0 caso não seja possível.
 
Exemplo:
ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])  
# Saída: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])  
# Saída: 0 (não há caminho possível)

Boa sorte e estamos à disposição para qualquer dúvida!
