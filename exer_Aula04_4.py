tot = 0
valor = 0
tot_idades = 0

while True:
    idade = int(input('Por favor, informe a sua idade: '))
    if (idade < 3 and idade != 0):
        print('Seu ingresso é gratuito!')
        tot += 1 
        tot_idades += idade
    elif (idade >=3 and idade <= 12):
        print('Seu ingresso custará R$ 15,00!')
        ing = 15
        tot += 1 
        tot_idades += idade
    elif (idade > 12):
        print('Seu ingresso custará R$ 30,00')
        ing = 30
        tot += 1 
        tot_idades += idade
    if (idade == 0):
        print('Você digitou um número inválido! Tente novamente...')
        break
    valor += ing

print(f'O valor total a ser pago é: R$ {valor}')
print(f'O total de ingressos é: {tot}')
print(f'A média de idade dos ingressos comprados é {tot_idades / tot}')