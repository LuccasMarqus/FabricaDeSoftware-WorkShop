idade = input('Digite sua idade: ')

try:
    if int(idade) >= 18:
        print('Você pode obter a CNH.')

    else: 
        print('Você não pode obter a CNH.')

except ValueError:
    print('Idade inválida.')