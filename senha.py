'''
Gerador de senhas aleatórias
autor: Gabriel Dai
2020

Utiliza o módulo random para gerar senhas aleatórias contendo letras maiúsculas, 
minúsculas, números e símbolos com base no código ASCII de cada caracter.
'''

import random

while True:

    senha = ''

    n = int(input('Quantos caracteres tem a senha? '))

    for i in range(n):
        t = random.randrange(4)

        # letras maiúsculas
        if t == 0 :
            senha += chr(random.randrange(65, 91))

        # letras minúsculas
        if t == 1:
            senha += chr(random.randrange(97, 123))

        # números
        if t == 2:
            senha += chr(random.randrange(48, 58))
        
        # símbolos
        if t == 3:
            senha += chr(random.randrange(33, 48))

    print(f'Sua senha é: {senha}')

    nova = input('Deseja criar uma nova senha? (s/n) ')

    if nova == 'n':
        break


    