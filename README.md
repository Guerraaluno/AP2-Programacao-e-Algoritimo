# 📦 Sistema de Cadastro e Relatório de Produtos

Este é um programa simples em Python que permite cadastrar 5 produtos com seus respectivos preços e, em seguida, exibe um relatório com o valor total, média de preços, produto mais caro e produto mais barato.

## 🚀 Funcionalidades

- Cadastro de **5 produtos** (nome e preço)
- Validação de entrada:
  - Nome não pode estar vazio
  - Preço não pode ser negativo e deve ser um número válido
- Cálculo do **valor total** dos produtos
- Cálculo da **média** de preços
- Identificação do **produto mais caro** e do **produto mais barato**
- Exibição clara de todos os produtos cadastrados e dos resultados

## 🧠 Estrutura do Código

O código é organizado em funções:

| Função                     | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `calcular_total(produtos)` | Soma os preços de todos os produtos no dicionário.                        |
| `produto_mais_caro(produtos)` | Retorna o nome e o preço do produto com maior valor.                    |
| `produto_mais_barato(produtos)` | Retorna o nome e o preço do produto com menor valor.                  |
| `media(total)`             | Calcula a média dividindo o total por 5 (quantidade fixa de produtos).    |
| `main()`                   | Função principal que executa o cadastro, validações e exibe o relatório.  |

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Salve o código em um arquivo, por exemplo: `cadastro_produtos.py`
3. Abra o terminal (ou prompt de comando) no diretório do arquivo.
4. Execute o comando:

```bash
python cadastro_produtos.py
```

ou

## 🐍 **Código Colab**
apenas clique no link e inicialize seu programa: https://colab.research.google.com/drive/1q3JMsxz8bb1eIHWlfBRuEB5Gd90zhhBD?usp=sharing
## 📝 Exemplo de Uso

CADASTRO DE 5 PRODUTOS

Produto 1:
Nome do produto: Café
Preço do produto (R$): 12.50

Produto 2:
Nome do produto: Leite
Preço do produto (R$): 6.30

...

RELATÓRIO DOS PRODUTOS

Produtos cadastrados:
  - Café: R$ 12.5
  - Leite: R$ 6.3
  ...

Valor total dos produtos: R$ 55.8
Média de preços: R$ 11.2
Produto mais caro: Café - R$ 12.5
Produto mais barato: Leite - R$ 6.3

## ⚠️ Observações
A quantidade de produtos é fixa em 5 (definida no loop for i in range(1, 6)).

O programa aceita números decimais com ponto (ex: 10.99).

Caso o usuário digite um valor inválido, o sistema solicita novamente até que a entrada seja correta.

## 📄 Licença
Este projeto é de uso livre para fins educacionais e de estudo.
Sinta-se à vontade para ajustar o conteúdo conforme a necessidade (por exemplo, adicionar seção de requisitos, autor, etc.).
