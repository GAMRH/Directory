print('------ Bem vindos a loja de Marmitas do Gabriel Augusto Muniz Regetz Herold ------')
print('---------------------------------- Cardápio --------------------------------------')
print('--------------| TAMANHO | BIFE ACEBOLADO (BA) | FILÉ DE FRANGO (FF) |-------------')
print('--------------|    P    |       R$ 16,00      |        R$ 15,00     |-------------')
print('--------------|    M    |       R$ 18,00      |        R$ 17,00     |-------------')
print('--------------|    G    |       R$ 22,00      |        R$ 21,00     |-------------')
print('--------------+-----------------------------------------------------+-------------')

vlr_pedido = 0

while True:
    sabor = input('Informe o sabor que deseja (BA/FF): ').upper()
    if sabor != 'BA' and sabor != 'FF': # caso o usuário digite algo diferente das opções apresentadas...
        print('\033[1;30;41mSabor inválido. Tente novamente...\033[m\n')
        continue # o programa volta para o início
    else: 
       tam = input('Informe o tamanho que deseja (P/M/G): ').upper()
       
       # cálculo do valor do pedido
       if tam == 'P' and sabor == 'BA':
          vlr_pedido += 16
          print('\033[1;33mVocê pediu um Bife Acebolado do tamanho P: R$ 16,00\033[m\n')
       elif tam == 'M' and sabor == 'BA':
          vlr_pedido += 18
          print('\033[1;33mVocê pediu um Bife Acebolado do tamanho M: R$ 18,00\033[m\n')
       elif tam == 'G' and sabor == 'BA':
          vlr_pedido += 22
          print('\033[1;33mVocê pediu um Bife Acebolado do tamanho G: R$ 22,00\033[m\n')
       elif tam == 'P' and sabor == 'FF':
          vlr_pedido += 15
          print('\033[1;33mVocê pediu um Filé de Frango do tamanho P: R$ 15,00\033[m\n')
       elif tam == 'M' and sabor == 'FF':
          vlr_pedido += 17
          print('\033[1;33mVocê pediu um Filé de Frango do tamanho M: R$ 17,00\033[m\n')
       elif tam == 'G' and sabor == 'FF':
          vlr_pedido += 21
          print('\033[1;33mVocê pediu um Filé de Frango do tamanho G: R$ 21,00\033[m\n')
       else:
              print('\033[1;30;41mTamanho inválido. Tente novamente...\033[m\n') # caso o usuário não digite o tamanho corretamente...
              continue # o programa volta para o início
           
    while True: # validação da resposta de mais pedidos        
        res = input('Deseja mais alguma coisa? (S/N): \n').upper()
    
        if (res == 'S' or res == 'N'):
          break # o programa só sai do laço se o usuário digitar uma resposta válida
        else:
          print('\033[1;30;41mOpção inválida! Tente novamente...\033[m')
       
    if (res == 'N'): # caso o usuário não queira mais nada...
          print(f'O valor total a ser pago é: \033[1;32mR$ {vlr_pedido:.2f}\033[m') # irá exibir o valor total do pedido
          break # sai do laço e encerra o programa
        
      
