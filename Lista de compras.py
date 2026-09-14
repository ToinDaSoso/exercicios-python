compras = []

print('-'*50)
print('COMPRAS')
print('-'*50)
print(' 1 - Adicionar produto \n 2 - Remover produto '
'\n 3 - Listar produtos \n 4 - sair')
print('-'*50)

while True:
    escolha = int(input('Digite a sua escolha: '))
    if escolha == 1:
        adicionar_produto = input('Adicione um produto: ').lower()
        compras.append(adicionar_produto)

    elif escolha == 2:
        remover_produto = input('Remova um produto: ').lower()
        if remover_produto in compras:
            compras.remove(remover_produto)                   
        else:
            print('Falta um acento ou o produto não está na lista!')  
              
    elif escolha == 3:
        if not compras:
            print('Sem itens na lista!')
        for indice, compra in enumerate(compras, start=1):
            print(f'{indice}. {compra}')
            
    elif escolha == 4:
        print('Saindo...')
        break
    
    elif escolha > 4:
        print('Escolha inválida!')