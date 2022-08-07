
import bancoPalavras as bp
from outrasfuncoes import *
from desenho import desenhaEnforcado


def jogo(palavra:str):
    palSecreta = ('_' * len(palavra))
    palSecreta = list(palSecreta)
    erros = 1
    while (erros<=6) and (palavra.upper() != ''.join(palSecreta).upper()):
        letra= input('Informe uma letra:')
        qtOcorrencias = len(buscaLetras(palavra, letra))
        if qtOcorrencias == 0:
            print('Não existe a letra: ', letra.upper())
            desenhaEnforcado(erros)
            erros += 1            
        else:
            print(f'Encontradas {qtOcorrencias} ocorrência da Letra {letra}')
        palForca = montarPalavraForca(palavra, letra)
        for i in range (len(palForca)):
            if palForca[i] != '*':
                palForca = list(palForca)
                palSecreta[i] = palForca[i]
        print(''.join(palSecreta))
    print('*** F I M ***')
    
  
print(bp.listaPalavras[sortearIndice()])
jogo(bp.listaPalavras[sortearIndice()])