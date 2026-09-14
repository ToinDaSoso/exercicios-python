import unicodedata

estoque = {
    'arroz': 10,
    'feijao': 5,
    'macarrao': 8,
    'cafe': 3
}

print(' 1 - Ver estoque\n 2 - Adiconar quantidade\n' \
' 3 - Remover quantidade\n 4 - Consultar produto\n 5 - Sair')

while True:
    escolha = int(input('Informe a sua escolha: '))
    if escolha == 1:
        print(estoque)

    elif escolha == 2:
        escolher_produto = input('Informe o produto que deseja adicionar uma quantidade: ').lower()
        escolher_produto = unicodedata.normalize('NFD', escolher_produto)
        sem_acento = []
        for caractere in escolher_produto:
             if not unicodedata.combining(caractere):
                  sem_acento.append(caractere)
        escolher_produto = ''.join(sem_acento)
        if escolher_produto in estoque:        
            quantidade = int(input(f'Informe a quantidade que será adicionada de {escolher_produto}: '))
            estoque[escolher_produto] = quantidade + estoque[escolher_produto]
        else:
            print('Produto não existe no estoque!')

    elif escolha == 3:
        escolher_produto = input('Informe o produto que deseja remover uma quantidade: ').lower()
        escolher_produto = unicodedata.normalize('NFD', escolher_produto)
        sem_acento = []
        for caractere in escolher_produto:
            if not unicodedata.combining(caractere):
                sem_acento.append(caractere)
        escolher_produto = ''.join(sem_acento)
        if escolher_produto in estoque:
            remover_quantidade = int(input(f'Informe a quantidade que será removida de {escolher_produto}: '))
            if remover_quantidade <= estoque[escolher_produto] and remover_quantidade > 0:
                estoque[escolher_produto] = estoque[escolher_produto] - remover_quantidade
            else:
                print(f'Quantidade de {escolher_produto} no estoque menor que a quantidade que deseja ser removida!')

    elif escolha == 4:
        consulta_produto = input('Informe o produto que deseja ser consultado: ').lower()
        consulta_produto = unicodedata.normalize('NFD',consulta_produto)
        sem_acento = []
        for caractere in consulta_produto:
            if not unicodedata.combining(caractere):
                sem_acento.append(caractere)
        consulta_produto = ''.join(sem_acento)                
        if consulta_produto in estoque:
            print(f'{consulta_produto}:', estoque[consulta_produto])
        else:
            print(f'{consulta_produto} não está no estoque!')

    elif escolha == 5:
        print('Saindo...')
        break

    elif escolha>5 or escolha <= 0:
        print('Escolha um número válido!')