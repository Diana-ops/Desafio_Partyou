# Desafio Partyou - Sistema de Gerenciamento de Clientes 

### O Desafio 
Criar um sistema para que um usuário administrador possa cadastrar, listar e despachar produtos e que um usuário cliente possa comprar e ver seus pedidos (incluindo seus status).

### Recursos Utilizados 

![Picture1](https://user-images.githubusercontent.com/46378210/70085829-ce41b080-15ef-11ea-8b9b-b4338302893d.png)

Parar desenvolver a aplicação, foi utilizado o sqlite3 para armazenar os dados em forma de arquivo a linguagem Python para gerenciar os dados e permitir com que o usuário navegue a partir de uma interface em console. 

### Construção do Banco de Dados 
O banco foi composto por 3 tabelas que armazenam:

_1. Dados referentes ao cadastro de usuários administradores e consumidores_

A tabela é composta por 3 colunas, que representam o tipo de usuário (ADM ou Consumidor), login e senha de acesso. Para entrar no sistema, o usuário deve apresentar um login presente no banco, caso contrário, deverá ser feito um __novo cadastro__.

![usuarios](https://user-images.githubusercontent.com/46378210/70085963-12cd4c00-15f0-11ea-96fd-ccb5760bee47.png)

_2. Lista de produtos_ 

A segunda tabela foi composta por 3 colunas, que representam o código do produto, seu nome e preço. 

![produtos](https://user-images.githubusercontent.com/46378210/70086047-45774480-15f0-11ea-938c-d3a885a730de.png)

_3. Lista de pedidos_

Esta tabela é composta por 5 colunas que representam:

3.1 Código: indica o indice do pedido.

3.2 Produto: indica o código do produto, que seria o mesmo apresentado na primeira coluna da lista de produtos.

3.3 Cliente: indica o nome do cliente.

3.4 Status: indica se o produto solicitado foi despachado (1) ou se ainda está em estoque (0)

3.5 Quantidade: indica a quantidade solicitada para o produto 

![pedidos](https://user-images.githubusercontent.com/46378210/70086048-45774480-15f0-11ea-9e9f-7493e88e41dd.png)



### Divisão dos Menus - Administrador e Consumidor 

A interface inicialmente apresenta a opção de acessar uma conta ou cadastra-la: 

![1](https://user-images.githubusercontent.com/46378210/70087789-b66c2b80-15f3-11ea-8138-a481a22d3c4e.png)

Ao cadastrar um novo usuário, é necessário inserir o tipo, login e senha:

![2](https://user-images.githubusercontent.com/46378210/70087790-b66c2b80-15f3-11ea-98f9-266d86c4e579.png)

Como consumidor, o usuário tem a opção de listar os produtos disponíveis, comprar e verificar o status dos pedidos:

![3](https://user-images.githubusercontent.com/46378210/70087792-b66c2b80-15f3-11ea-9742-a098727442f2.png)

Realizando o login como adiminstrador, o usuário tem a opção de listar e cadastrar novos produtos além de despachar e listar pedidos:  

![4](https://user-images.githubusercontent.com/46378210/70087788-b66c2b80-15f3-11ea-9987-2ec52028657b.png)


