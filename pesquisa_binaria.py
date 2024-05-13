#algoritimo de busca binaria
def pesquisa_binaria(lista, item):    
    numero_baixo = 0
    numero_alto = len(lista) - 1

    while numero_baixo <= numero_alto:
        meio = (numero_baixo + numero_alto) // 2  
        chute = lista[meio]  
        if chute == item:
            return meio
        if chute > item:
            numero_alto = meio - 1
        else:
            numero_baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 7))
