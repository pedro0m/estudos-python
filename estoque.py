def calcular_patrimonio(estoque):
    subtotal = [item['preco'] * item['qtd'] for item in estoque]
    return sum(subtotal)

def verificar_estoque_baixo(estoque, limite):
    estoque_baixo = [item['nome'] for item in estoque if item['qtd'] < limite]
    return estoque_baixo

def adicionar_produto(estoque, codigo, nome, preco, qtd):
    estoque.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'qtd': qtd})

estoque = [
    {'codigo': 'P01', 'nome': 'Teclado Mecânico', 'preco': 250.0, 'qtd': 12},
    {'codigo': 'P02', 'nome': 'Mouse Gamer', 'preco': 120.0, 'qtd': 3},
    {'codigo': 'P03', 'nome': 'Monitor 24"', 'preco': 890.0, 'qtd': 5},
    {'codigo': 'P04', 'nome': 'Cabo HDMI', 'preco': 35.0, 'qtd': 2},
    {'codigo': 'P05', 'nome': 'Headset USB', 'preco': 180.0, 'qtd': 8}
]    

while True:
    print('''[ 1 ] - Patrimonio
[ 2 ] - Alerta de Estoque
[ 3 ] - Cadastro
[ 4 ] - Mostrar estoque atualizado
[ 5 ] - Sair''')
    opcao = input('Digite uma opção: ')

    if opcao == '1':
        print('Total de patrimonio em estoque:')
        print(f'R$ {calcular_patrimonio(estoque):.2f}')

    elif opcao == '2':
        print('Os seguintes itens estão com o estoque baixo:')
        items = verificar_estoque_baixo(estoque, 5)

        for i in range(len(items)):
            print(i+1, '-', items[i])
            i =+ 1
        
    elif opcao == '3':
        codigo = input('Digite o código do produto: ')
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        qtd = int(input('Digite a quantidade de produtos: '))
        adicionar_produto(estoque, codigo, nome, preco, qtd)
        print('Produto adicionado com sucesso!')

    elif opcao == '4':
        for item in estoque:
            print('Produto:', item['nome'], 'Preço:', item['preco'], 'Quantidade:', item['qtd'])
        
    elif opcao == '5':
        print('Saindo...')
        break

    else:
        print('Digite uma opção válida.')