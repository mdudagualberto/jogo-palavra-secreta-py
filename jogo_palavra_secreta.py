import os
palavra_secreta= input('Escolha uma palavra secreta: ')
repeticoes= 0
palavra_atual= len(palavra_secreta) * '*'
os.system('clear')
while True:
    indice= 0
    resposta= input('Digite uma letra: ')

    if len(resposta) > 1:
        print('Digite apenas uma letra')
        repeticoes += 1
        continue
    if resposta not in palavra_secreta:
        print('Essa letra não está na palavra secreta')
        repeticoes += 1
        continue

    for letra in palavra_secreta:
        if resposta==letra:
            palavra_atual= palavra_atual[:indice] + letra + palavra_atual[indice + 1:]
        indice += 1
    repeticoes += 1

    if palavra_atual== palavra_secreta:
            print(f'Você acertou a palavra em {repeticoes} repetições')
            print(f'A palavra era {palavra_atual}')
            break
    print(palavra_atual)