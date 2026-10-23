vendas = {}
numero_venda = 0
while True:
    print('''===== SISTEMA DE VENDAS =====
1 - Registrar venda
2 - Listar vendas
3 - Consultar vendas acima de R$ 100
4 - Exibir relatório
5 - Encerrar''')
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        numero_venda += 1
        compra = {}
        while True:
            produto_nome = input('Digite o nome do produto: ')
            if produto_nome != '':
                compra['Produto'] = produto_nome
                break
            else:
                print('O nome não pode ficar vazio.')
        
        while True:
            quantidade = input('Digite a quantidade de produtos: ')
            if quantidade != '' and not quantidade == '0':
                compra['Quantidade'] = int(quantidade)
                break
            else:
                print('A quantidade não pode estar vazia e deve ser maior que 0')

        while True:
            valor_unitario = input('Digite o valor unitário do produto: ')
            if valor_unitario != '' and not valor_unitario == '0':
                compra['Preço Unitário'] = float(valor_unitario)
                break
            else:
                print('O preço não pode estar vazio e deve ser maior que 0')

        valor_total = int(quantidade) * float(valor_unitario)
        compra['Total'] = float(valor_total)

        vendas[f'Venda_{numero_venda}'] = compra
        print('Venda registrada com sucesso!')

    elif opcao == '2':
        if vendas != {}:
            for numero, item_venda in vendas.items():
                print(numero)
                for n, v in item_venda.items():
                    print(f'{n}: {v}')
                print('')
        else:
            print('Não há nenhuma venda')

    elif opcao == '3':
        if vendas != {}:
            acima_cem = [chave for chave, valor in vendas.items() if valor['Total'] > 100]
            for venda in acima_cem:
                print(venda)
        else:
            print('Não há nenhuma venda')
    
    elif opcao == '5':
        break
    else:
        print('Opção inválida.')
        