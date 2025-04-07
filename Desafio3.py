def ladderLength(inicio, fim, lista):
    tem_fim = False
    i = 0
    while i < len(lista):
        if lista[i] == fim:
            tem_fim = True
            break
        i += 1
    
    if not tem_fim:
        return "0 (não há caminho possível)"
    novaLista = set()

    j = 0
    while j < len(lista):
        novaLista.add(lista[j])
        j += 1

    fila = []
    fila.append((inicio, [inicio]))
    
    while len(fila) > 0:
        atual, caminho = fila.pop(0)
        
        pos = 0
        while pos < len(atual):
            letra = 'a'
            while letra <= 'z':
                nova = atual[:pos] + letra + atual[pos+1:]
                if nova == fim:
                    caminho_completo = caminho + [fim]
                    passos = len(caminho_completo)
                    caminhoFinal = " -> ".join(caminho_completo)
                    return f'{passos} ("{caminhoFinal}")'

                if nova in novaLista:
                    fila.append((nova, caminho + [nova]))
                    novaLista.remove(nova)
                
                letra = chr(ord(letra) + 1) 
            pos += 1
    
    return "0 (não há caminho possível)"


resultado = ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(resultado)
resultado = ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print(resultado)