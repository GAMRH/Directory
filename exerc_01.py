print('---------- Bem-vindos à loja do Gabriel Augusto Muniz Regetz Herold ----------\n')

valorDoPedido = float(input('Informe o valor do pedido: R$ '))
quantidadeParcelas = int(input('Informe a quantidade de parcelas: '))

# irá definir a porcentagem de juros baseado na quantidade de parcelas
if (quantidadeParcelas < 4):
    juros = (0/100)
elif (quantidadeParcelas >= 4 and quantidadeParcelas <6 ):
    juros = (4/100)
elif (quantidadeParcelas >= 6 and quantidadeParcelas <9 ):
    juros = (8/100)
elif (quantidadeParcelas >= 9 and quantidadeParcelas <13 ):
    juros = (16/100)
else:
    juros = (32/100)
    
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas # cálculo do valor das parcelas
valorTotalParcelado  = valorDaParcela * quantidadeParcelas # cálculo do valor total do pedido

print(f'O valor das parcelas é: \033[1;32mR$ {valorDaParcela:.2f}\033[m') # irá exibir o valor de cada parcela com duas casas decimais
print(f'O valor total parcelado é: \033[1;32mR$ {valorTotalParcelado:.2f}\033[m') # irá exibir o valor total do pedido com duas casas decimais