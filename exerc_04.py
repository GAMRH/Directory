def cadastrar_funcionario(id):
  '''
  Função para cadastrar novos funcionários!
  '''
  global lista_funcionarios
  global id_global
  nome = input('Informe o nome do funcionário: ').capitalize()
  setor = input('Informe o setor do funcionário: ').capitalize()
  salario = float(input('Informe o salário do funcionário: R$ '))
  novo_func = {'id': id,
               'nome': nome,
               'setor': setor,
               'salario': salario
               }
  lista_funcionarios.append(novo_func.copy()) # estou adicionando na lista de funcionários uma cópia das informações do novo funcionário
  print('\033[1;30;42mFuncionário cadastrado com sucesso!\033[m\n')

def consultar_funcionarios():
    '''
    Função utilizada para consultar os funcionários, conforme necessidade do usuário!
    '''
    while True:
      print('-------------------- \033[1mMENU - CONSULTA FUNCIONÁRIO\033[m ------------------------')
      try:
        op = int(input('Escolha a opção desejada:\n 1 - Consultar Todos\n 2 - Consultar por Id\n 3 - Consultar por Setor\n 4 - Retornar ao menu\n')) # Menu - Consulta Funcionários
        if op == 1: # se o usuário decidir consultar todos os funcionários...
          if lista_funcionarios:
            for novo_func in lista_funcionarios:
              print(f'ID: \033[1;33m{novo_func["id"]}\033[m\nNome: {novo_func["nome"]}\nSetor: {novo_func["setor"]}\nSalário: R$ {novo_func["salario"]:.2f}\n')
          else:
            print('\033[1;30;41mNenhum funcionário foi encontrado no cadastro!\033[m\n')
            
        elif op == 2: # se o usuário decidir consultar por ID...
          id = int(input('Informe o ID do funcionário: '))
          func_existe = False
          for novo_func in lista_funcionarios:
            if id == novo_func["id"]:
              print(f'ID: \033[1;33m{novo_func["id"]}\033[m\nNome: {novo_func["nome"]}\nSetor: {novo_func["setor"]}\nSalário: R$ {novo_func["salario"]:.2f}\n')
              func_existe = True
              break
          if not func_existe:
              print('\033[1;30;41mNão foi encontrado nenhum funcionário com esse ID!\033[m\n')
              
        elif op == 3: # se o usuário decidir consultar por setor...
          setor = input('Informe o setor do funcionário: ').capitalize()
          func_existe = False
          for novo_func in lista_funcionarios:
            if setor == novo_func["setor"]:
              print(f'ID: \033[1;33m{novo_func["id"]}\033[m\nNome: {novo_func["nome"]}\nSetor: {novo_func["setor"]}\nSalário: R$ {novo_func["salario"]:.2f}\n')
              func_existe = True
          if not func_existe:
              print('\033[1;30;41mNão foram encontrados funcionários cadastrados no setor informado!\033[m\n')
              
        elif op == 4: # se o usuário quiser retornar ao menu...
          return
        else:
          print('\033[1;30;41mOpção inválida!\033[m\n')
          continue
      except ValueError:
        print('\033[1;30;41mPor favor, insira um valor válido...\033[m\n')

def remover_funcionario():
    '''
    Função para remover algum funcionário cadastrado, baseado no ID de cada funcionário.
    '''
    if not lista_funcionarios: # caso não for encontrado nenhum funcionário cadastrado...
      print('\033[1;30;41mNão há funcionários cadastrados para serem removidos!\033[m\n')
      return

    while True:
        print('------------------ \033[1mMENU - REMOVER FUNCIONÁRIO\033[m ----------------------')
        try:
          for novo_func in lista_funcionarios:
            id = int(input('Informe o ID do funcionário: '))
            if id == novo_func["id"]:
              lista_funcionarios.remove(novo_func)
              print('\033[1;30;42mFuncionário removido com sucesso!\033[m\n')
              return
            else:
              print('\033[1;30;41mID Inválido!\033[m\n')
              continue
        except ValueError:
          print('\033[1;30;41mPor favor, insira um valor válido...\033[m\n')


# PROGRAMA PRINCIPAL
lista_funcionarios = []
id_global = 4955404

print('------ Bem vindos a empresa do Gabriel Augusto Muniz Regetz Herold ------')

while True:
  print('--------------------------- \033[1mMENU PRINCIPAL\033[m ------------------------------')
  try:
    alt = int(input('Escolha a opção desejada:\n 1 - Cadastrar Funcionários\n 2 - Consultar Funcionário(s)\n 3 - Remover Funcionário\n 4 - Encerrar Programa\n')) # Menu Principal
    if alt == 1: # se o usuário decidir cadastrar novos funcionários...
      id_global += 1 # será incrementado um número à variável "id_global" e será o ID do novo funcionário...
      print('------------------- \033[1mMENU - CADASTRO DE FUNCIONÁRIO\033[m ----------------------')
      print(f'ID do funcionário: \033[1;33m{id_global}\033[m')
      cadastrar_funcionario(id_global)
    elif alt == 2: # se o usuário decidir consultar os dados dos seus funcionários...
      consultar_funcionarios()
    elif alt == 3: # se o usuário decidir remover os dados de algum funcionário...
      remover_funcionario()
    elif alt == 4: # se o usuário quiser sair do programa...
      print('Encerrando o programa...')
      break
    else:
      print('\033[1;30;41mOpção inválida! Tente novamente...\033[m\n')
  except ValueError:
      print('\033[1;30;41mPor favor, insira um valor válido...\033[m\n')
    
    
    



