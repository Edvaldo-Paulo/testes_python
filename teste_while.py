nome = input('Informe seu nome: ')

confirma_nome = input('Confirme seu nome: ')


contador = 1

while contador <= 3:
    if nome != confirma_nome:
        print('Você digitou o nome incorreto. Tente novamente!')
        confirma_nome = input()
        contador = contador + 1
    else:
        break

if contador > 3:
    print('Você excedeu o número de tentativas!')
else:
    print('Login efetuado com sucesso!')


