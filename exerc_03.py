def escolha_modelo():
  '''
  Função criada para retornar o valor da camiseta escolhido pelo usuário!
  '''
  while True:
       try:
         print('--------------+--------------------------------------------------------+-------------')
         print('--------------|  SIGLA  |         MODELOS         |        PREÇOS      |-------------')
         print('--------------|   MCS   |   MANGA CURTA SIMPLES   |       R$ 1,80      |-------------')
         print('--------------|   MLS   |   MANGA LONGA SIMPLES   |       R$ 2,10      |-------------')
         print('--------------|   MCE   | MANGA CURTA COM ESTAMPA |       R$ 2,90      |-------------')
         print('--------------|   MLE   | MANGA LONGA COM ESTAMPA |       R$ 3,20      |-------------')
         print('--------------+--------------------------------------------------------+-------------')
         modelo = input('Informe a sigla do modelo desejado: ').upper()
         if modelo == 'MCS':
            return 1.80
         elif modelo == 'MLS':
            return 2.10
         elif modelo == 'MCE':
            return 2.90
         elif modelo == 'MLE':
            return 3.20
         else: # caso o valor inserido não seja nenhuma das opções apresentadas...
           print('\033[1;33mPor favor, informe a sigla corretamente...\033[m\n')
       except ValueError:
           print('\033[1;30;41Você digitou um valor inválido! Tente novamente...\033[m\n') 
           
def num_camisetas():
   '''
   Função criada para retornar o número de camisetas do pedido com desconto!
   '''
   desconto = 0
   while True:
      try:
         qtd = int(input('Informe a quantidade de camisetas que deseja adquirir deste modelo: '))
         if qtd < 20:
            desconto = (0/100)
         elif (qtd >= 20) and (qtd < 200):
            desconto = (5/100)
         elif (qtd >= 200) and (qtd < 2000):
            desconto = (7/100)
         elif (qtd >= 2000) and (qtd <= 20000):
            desconto = (12/100)
         else: # caso o valor inserido seja maior do que 20000...
           print('\033[1;30;41mNão aceitamos pedidos com essa quantidade de camisetas!\033[m\n')
           continue 
      except ValueError: # caso nao digite um valor inteiro...
            print('\033[1;30;41mVocê digitou um valor inválido! Tente novamente...\033[m\n') 
            
      return qtd - (qtd * desconto)
   
def frete():
    '''
    Função criada para retornar o valor do frete escolhido pelo usuário!
    '''
    while True:
      try:
        print('--------------+---------------------------------------------------------+-------------')
        print('--------------| OPÇÃO |         FRETE         |        VALOR EXTRA      |-------------')
        print('--------------|   1   |     TRANSPORTADORA    |         R$ 100,00       |-------------')
        print('--------------|   2   |         SEDEX         |         R$ 200,00       |-------------')
        print('--------------|   0   |   RETIRAR NA FÁBRICA  |          GRÁTIS         |-------------')
        print('--------------+---------------------------------------------------------+-------------')
        op = int(input('Informe a opção do serviço de frete que deseja contratar: '))
        if op == 1:
           return 100
        elif op == 2:
           return 200
        elif op == 0:
           return 0
        else: # caso o usuário não insira um valor inteiro que seja válido...
           print('\033[1;30;41mEscolheu uma opção inválida. Tente novamente...\033[m\n')
           continue
      except ValueError: # caso o usuário não insira um valor inteiro...
           print('\033[1;30;41mPor favor, insira um valor inteiro!\033[m\n')
           
    
# PROGRAMA PRINCIPAL
print('------ \033[1mBem vindos à Fábrica de Camisetas do Gabriel Augusto Muniz Regetz Herold \033[m-----')
vlr_camisa = escolha_modelo() # Essa variável vai receber o valor retornado por essa funcao
camisaCDesc = num_camisetas() # Essa variável irá receber o valor que foi calculado na funcao para o número de camisetas com desconto
trans = frete() # Essa variável vai receber o valor retornado da funcao 'frete()'
total = (vlr_camisa * camisaCDesc) + trans # A variável vai receber o valor total que foi calculado 

print(f'Total: \033[1;32mR$ {total:.2f}\033[m (Modelo: \033[1;36mR$ {vlr_camisa}\033[m * Quantidade (com desconto): \033[1;34mR$ {camisaCDesc}\033[m + frete: \033[1;33mR$ {trans}\033[m)')
       