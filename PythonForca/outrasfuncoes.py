import random
import bancoPalavras as bp

def sortearIndice() -> int:
    return (random.randint(0, len(bp.listaPalavras)-1))
    

def montaListaLetras(palavra) -> list:
    listaLetras = []
    for letra in palavra:
        listaLetras.append(letra.upper())
    return listaLetras

def buscaLetras(palavra, procura) -> list:
    indices = []
    for indice in range(len(palavra)):
        if palavra[indice].upper() == procura.upper():
            indices.append(indice)
    return indices


def montarPalavraForca(palavra, letra) -> str:
    descoberta = ''
    print("\n\n")
    for caracter in palavra:
        if caracter.upper() == letra.upper():
            descoberta += letra.upper()
        else:
            descoberta += "*"
    print(descoberta)
    return descoberta


