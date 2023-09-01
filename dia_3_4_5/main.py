from funcoes import soma, print_subtracao, soma_sem_parametro

num = input("Digite um número: ")
num2 = input("Digite outro número: ")

num =  float(num)
num2 = float(num2)

resultado = soma(x = num, y = num2)

print(f"Resultado: {resultado}")