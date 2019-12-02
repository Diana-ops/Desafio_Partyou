"""
Desafio Backend - Partyou
@Autor: Diana Regina da Silva
E-mail: dianaregina22@outlook.com.br
Linguagem: Python 3.5
Entrega do Projeto: 02/12/2019
"""

import sqlite3 #Biblioteca para manipular o banco de dados 

#Conexão com o banco
conn = sqlite3.connect('gerenciamento.db')
cursor = conn.cursor()

# -- Listas para Armazenamento de Pedidos e Produtos -- #
produtos = list() #Código, nome e preço do produto 
pedidos = list() #Código da venda, produto, consumidor e status da compra 

#Requisição das tabelas no banco
cursor.execute("SELECT * FROM pedidos")
for pedido in cursor.fetchall():
    pedidos.append(pedido)
 
cursor.execute("SELECT * FROM produtos")
for produto in cursor.fetchall():
    produtos.append(produto)

user = False

# --- Funções --- #

# -- Requisição -- #
def mostrar_produtos():
    if len(produtos[0]) > 0:
        print("Lista de Produtos Disponíveis")
        print()
        print("Codigo - Nome do Produto - Preço")
        for produto in produtos:
            print(" ", produto[0]," ", produto[1].capitalize(), " R$ ", produto[2])     
            print()
    else:
        print("Não há produtos cadastrados")
		  
while True: 
  conn.close()  
  conn = sqlite3.connect('gerenciamento.db')
  cursor = conn.cursor()
  # ---- Acesso ao Administrador/Consumidor ---- #
  
  if user == False:
    opcao = input("Entrar [E] - Cadastro [C]: ").lower()
    
    # --- Cadastro --- #
    if opcao == "c":
        
        tipo = input("Tipo do Conta: Administrador [ADM] ou Consumidor [CONSU]?").lower()
        login = input("Digite o nome do novo usuário: ").lower()
        senha = input("Digite sua senha de acesso: ").lower()
        
        cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?);", (tipo, login, senha))
        conn.commit()
        
        if cursor.fetchall() != 0:
            print("\nO usuário ", login.capitalize(), "foi cadastrado no sistema como", tipo.upper())
            
    # --- Acessar Conta --- #   
    if opcao == "e":
        login = input("Digite seu Login: ").lower()
        senha = input("Digite sua Senha: ").lower()
        
        cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha = ?;", (login, senha))
        for acesso in cursor.fetchall():
          user = acesso[0]
          print("Usuario Logado!")
          
        if user == False:
          print("Login ou Senha invalidos, tente novamente!")
          
        
          
  if (user == "adm" or user == "consu"):
          # --- Opções para o Administrador --- #
          
          if user == "adm":
            print("Sistema de Gerenciamento de Compras (SGS)\n")
            
            print("\nBem Vindo, ADM ", login.capitalize())
            print()
            print("Cadastrar novo produto [C]")
            print("Listar Produtos [LP]")
            print("Listar Pedidos [LD]")
            print("Despachar Pedidos [DP]")
            print("Sair [S]")
        
            opcao = input("").lower()
        
            # --- Inserindo Novo Produto --- #
            if opcao == "c":
              nome_produto = input("Insira o nome do produto: ")
              preco_produto = float(input("Insira o preço deste produto: "))
              cursor.execute("INSERT INTO produtos VALUES(?, ?, ?);", (len(produtos)+1, nome_produto, preco_produto))
              conn.commit()
              if cursor.fetchall() != 0:
                  print("O produto ", nome_produto, " R$ ", preco_produto, " foi inserido no sistema")
                  
            
            # --- Listando Produtos --- #
            if opcao == "lp":
              mostrar_produtos()
              
              
             
            # --- Listando Pedidos --- #
            if opcao == "ld":
                if len(pedidos) > 0:
                    print("Lista de Pedidos")
                    print()
                    print("Codigo - Código do Produto - Comparador - Status - Quantidade")
                    for pedido in pedidos:
                        print(pedido)
                        print()
                else:
                    print("Não há produtos cadastrados")
            
            # --- Despachando Produtos --- #
            if opcao == "dp":
                status = False #Verifica se há pedidos a serem despachados
                print("Lista de Pedidos a Despachar:\n")
                print("Número do Pedido - Código do Produto - Consumidor - Quantidade")
                for pedido in pedidos:
                    if pedido[3] == 0:
                        print(pedido)
                        status = True
                if status == True: 
                    desp = int(input("Digite o numero do pedido a ser despachado: "))
                    cursor.execute("UPDATE pedidos SET status=1 WHERE codigo = {};".format(desp))
                    conn.commit()
                    if cursor.fetchall() !=0:
                        print("O pedido ", desp, "foi despachado!")
                else:
                    print("Não há pedidos para despachar, todos foram entregues.")
            
            # -- Voltando ao Menu -- #
            if opcao == "s":
              user = False
              print(" ... Voltando para o Menu ... ")
        
            
          # --- Opções para o Consumidor --- # 
          if user == "consu":
            print("Sistema de Gerenciamento de Compras (SGS)\n")
           
            print("\nBem Vindo, Consumidor ", login.capitalize())
            print()
            print("Mostrar Produtos [MC]")
            print("Comprar [C]")
            print("Ver meus pedidos e status [VP]")
            print("Sair [S]")
        
            opcao = input("").lower()
        
            # -- Voltando ao Menu -- #
            if opcao == "s":
              user = False
              print(" ... Voltando para o Menu ... ")
             
            # -- Mostrar Produtos -- #
            if opcao == "mc":
              # -- Listando Produtos Disponíveis -- #
              mostrar_produtos()
            
            # --- Ver os pedidos --- #
            if opcao == "vp":
                for pedido in range(len(pedidos)):
                    
                    if pedidos[pedido][2] == login:
                        print("Pedido: ", produtos[pedido][1].capitalize(), " Quantidade: ", pedidos[pedido][4], " Status: ", pedidos[pedido][3])
        
            # --- Comprar --- #
            
            if opcao == "c":
              # -- Listando Produtos Disponíveis -- #
              mostrar_produtos()
        
              escolha = int(input("Digite o item do produto desejado: "))
              quantidade = int(input("Digite a quantidade desejada: "))
        
              print("Produto escolhido: ", produtos[escolha-1][1].capitalize(), "\nTotal a Pagar: R$ {} ". format(produtos[escolha-1][2]*quantidade))
              confirmar = input("Confirmar a Compra? [S][N]\n").lower()
              
              if confirmar == "s":
                  for i in range(len(produtos)):
                      if escolha == produtos[i][0]: #Se houver o código cadastrado
                              cursor.execute("INSERT INTO pedidos VALUES(null, ?, ?, 0, ?);", (escolha, login, quantidade))
                              conn.commit()
                              if cursor.fetchall() != 0:
                                  print("O pedido foi concluido com sucesso!\n")
                                  print("Produto escolhido: ", produtos[escolha-1][1].capitalize(), "\nTotal a Pagar: R$ {} ". format(produtos[escolha-1][2]*quantidade))

    
conn.close()            