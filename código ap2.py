#calcula o total dos produtos
def calcular_total(produtos):
    return sum(produtos.values())

#encontra o produto mais caro na lista de produtos
def produto_mais_caro(produtos):
    nome_caro = max(produtos, key=produtos.get)
    return nome_caro, produtos[nome_caro]

#encontra o produto mais barato na lista de produtos
def produto_mais_barato(produtos):
    nome_barato = min(produtos, key=produtos.get)
    return nome_barato, produtos[nome_barato]

#calcula a media dos produtos
def media(total):
    return total / 5


def main():
    produtos = {}

    print("CADASTRO DE 5 PRODUTOS")

    #delimita o limite de itens a ser cadastrados
    for i in range(1, 6):
        print(f"\nProduto {i}:")

        #adiciona nome enquanto i estiver na range
        while True:
            nome = input("Nome do produto: ").strip()
            if nome == "":
                print("Erro: o nome não pode ficar vazio. Digite novamente.")
            else:
                break
        #adiciona preço enquanto o bloco de adicionar nome estar verdadeiro
        while True:
            try:
                preco = float(input("Preço do produto (R$): "))
                if preco < 0:
                    print("Erro: o preço não pode ser negativo. Digite novamente.")
                else:
                    break
            except ValueError:
                print("Valor inválido. Digite um número (use ponto para decimais).")

        produtos[nome] = preco

    print("\nRELATÓRIO DOS PRODUTOS")

    print("\nProdutos cadastrados:")
    for nome, preco in produtos.items():
        print(f"  - {nome}: R$ {preco:.1f}")

    total = calcular_total(produtos)
    media_valor = media(total)
    nome_caro, preco_caro = produto_mais_caro(produtos)
    nome_barato, preco_barato = produto_mais_barato(produtos)

    print(f"\nValor total dos produtos: R$ {total:.1f}")
    print(f"Média de preços: R$ {media_valor:.1f}")
    print(f"Produto mais caro: {nome_caro} - R$ {preco_caro:.1f}")
    print(f"Produto mais barato: {nome_barato} - R$ {preco_barato:.1f}")



main()
