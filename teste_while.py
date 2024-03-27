email = 'andrevieira00@gmail.com'
senha = '1234'
confirma_email = input('Confirme seu e-mail: ')
confirma_senha = input('Confirme sua senha: ')

contador = 1
verificador = [confirma_email, confirma_senha]

while contador <= 3:
    if email != confirma_email:
        print('Você digitou o nome incorreto. Tente novamente!')
        confirma_email = input()
        contador += 1
    elif senha != confirma_senha:
        print('Você digitou a senha incorreta. Tente novamente!')
        confirma_senha = input()
        contador += 1
    elif verificador:
        print('Você digitou o nome e senha incorretos. Tente novamente!')
        confirma_email = input('Confirme o e-mail:')
        confirma_senha = input('Confirme a senha: ')
        contador += 1
    else:
        break

if contador > 3:
    print('Você excedeu o número de tentativas!')
else:
    print('Login efetuado com sucesso!')


