email = 'andrevieira00@gmail.com'
senha = '1234'
confirma_email = input('Confirme seu e-mail: ')
confirma_senha = input('Confirme sua senha: ')

contador = 1



while contador <= 3:
    
    if email != confirma_email and senha != confirma_senha:
        print('Você digitou o e-mail incorreto. Tente novamente!')
        confirma_email = input('Confirme o e-mail: ')
        print('Você digitou a senha incorreta. Tente novamente!')
        confirma_senha = input('Confirme a senha: ')
        contador += 1

    elif confirma_email != email or confirma_senha != senha:
        if email != confirma_email:
            print('Você digitou um e-mail incorreto. Tente novamente!')
            confirma_email = input('Confirme o e-mail:')
            contador += 1
            
        else:
            print('Você digitou uma senha incorreta. Tente novamente')
            confirma_senha = input('Confirme a senha: ')
            contador += 1

    else:
        break

if contador > 3:
    print('Você excedeu o número de tentativas!')
else:
    print('Login efetuado com sucesso!')


