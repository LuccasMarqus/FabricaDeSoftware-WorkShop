velocidade = input("Velocidade do automovel: ")

try:
    velocidade = float(velocidade)

    if velocidade > 80:
            acima = velocidade - 80
            multa = 7 * acima
            print(f"Você excedeu o limite de 80Km/h, o valor da multa é de R${multa:.2f}")

    else:
        print("Você não excedeu o limite de 80Km/h.")

except ValueError:
     print("Valor inválido.")



