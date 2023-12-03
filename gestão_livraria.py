livros = []  # Lista de livros (tuplas)
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar livro \n'
    '2. Remover livro \n'
    '3. Atualizar informações do livro \n'
    '4. Listar livros disponíveis \n'
    '5. Sair \n')

print(menu)

while escolha != 5:
    escolha = int(input('Informe a opção: '))

    if escolha == 1:
        titulo = input('Informe o título do livro: ')
        autor = input('Informe o autor do livro: ')
        preco = float(input('Informe o preço do livro: '))
        quantidade = int(input('Informe a quantidade em estoque: '))
        livros.append((titulo, autor, preco, quantidade))
        print(f'O livro "{titulo}" foi adicionado ao estoque.')

    elif escolha == 2:
        titulo = input('Informe o título do livro a ser removido: ')
        for livro in livros:
            if livro[0] == titulo:
                livros.remove(livro)
                print(f'O livro "{titulo}" foi removido do estoque.')
                break
        else:
            print(f'O livro "{titulo}" não encontrado no estoque.')

    elif escolha == 3:
        titulo = input('Informe o título do livro a ser atualizado: ')
        for livro in livros:
            if livro[0] == titulo:
                preco = float(input('Informe o novo preço do livro: '))
                quantidade = int(input('Informe a nova quantidade em estoque: '))
                livro = (titulo, livro[1], preco, quantidade)
                print(f'As informações do livro "{titulo}" foram atualizadas.')
                break
        else:
            print(f'O livro "{titulo}" não encontrado no estoque.')

    elif escolha == 4:
        if len(livros) == 0:
            print('Não há livros disponíveis!')
        else:
            print('Livros disponíveis:')
            for livro in livros:
                titulo, autor, preco, quantidade = livro
                print(f'Título: {titulo}, Autor: {autor}, Preço: R${preco:.2f}, Estoque: {quantidade}')

    elif escolha == 5:
        print("Aplicativo encerrado.")
        break

    else:
        print('Opção inválida')
