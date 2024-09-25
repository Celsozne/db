from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['loja']
collection = db['coisas']


def criar_produto():
    nome = input("Nome do produto: ")
    preco = input("Preco do produto")
    estoque = input("Estoque do produto")

    novo_produto = {
        'nome': nome,
        'preco': preco,
        'estoque': estoque,
        'data': datetime.now()
    }
    result = collection.insert_one(novo_produto)

    if result.inserted_id:
        print(f"Produto {nome} criado com sucesso!")
    else:
        print("erro")


def buscar_produtos():
    produtos = collection.find()
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preco: {produto['preco']}")
        print(f"Estoque: {produto['estoque']}")
        print(f"Data: {produto['data']}")


def alterar_produto():
    nome_antigo = input("Nome do produto a ser alterado: ")

    nome_novo = input("Novo nome do produto: ")
    preco_novo = input("Novo preco do produto: ")
    estoque_novo = input("Novo estoque do produto: ")

    novos_dados = {
        'nome': nome_novo,
        'preco': preco_novo,
        'estoque': estoque_novo,
    }

    result = collection.update_one(
        {'nome': nome_antigo},
        {'$set': novos_dados}
    )

    if result.modified_count > 0:
        print(f"Produto {nome_antigo} alterado com sucesso!")
    else:
        print("erro")


def deletar_produto():
    nome_produto = input("Digite o nome do produto que deseja deletar: ")

    resultado = collection.delete_one({'nome': nome_produto})  # Filtrar pelo nome do produto

    if resultado.deleted_count > 0:
        print(f"Produto '{nome_produto}' foi deletado com sucesso.")
    else:
        print("erro")


def main():
    while True:
        print("1 - criar produto")
        print("2 - buscar produtos")
        print("3 - alterar produto")
        print("4 - deletar produto")
        print("5 - sair")

        escolha = input("Escolha a operacao: ")

        opcao = {
            '1': criar_produto,
            '2': buscar_produtos,
            '3': alterar_produto,
            '4': deletar_produto,
            '5': sair
        }

        funcao = opcao.get(escolha)

        if funcao:
            funcao()
    else:
        print("Opção inválida. Tente novamente.")

    if funcao == '5':
        sair()


def sair():
    print("Saindo do programa...")
    main()


main()
