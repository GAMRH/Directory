# Exercicio 3
print('Bem vindo ao nosso programa! \nVamos calcular o custo pelo fornecinecimento de energia...')

qtcon = float(input('Informe a quantidade de kWh consumida: '))
tpi = input('Informe o tipo de instalação da rede: \n R - Residencial \n C - Comercial \n I - Industrial \n')

if((tpi == 'R' or 'r') and (qtcon <= 500)):
   custo = qtcon * 0.40
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
elif ((tpi == 'R' or 'r') and (qtcon > 500)):
   custo = qtcon * 0.65
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
elif((tpi == 'C' or 'c') and (qtcon <= 1000)):
   custo = qtcon * 0.55
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
elif((tpi == 'C' or 'c') and (qtcon > 1000)):
   custo = qtcon * 0.60
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
elif ((tpi == 'I' or 'i') and (qtcon <= 5000)):
   custo = qtcon * 0.55
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
elif((tpi == 'I' or 'i') and (qtcon > 5000)):
   custo = qtcon * 0.60
   print(f'O custo do fornecimento de energia nesse caso é: {custo}')
else: 
   print('Você digitou alguma informação inválida! Tente novamente...')