import csv

from regras_ofertas import produto_permitido


ARQUIVO_ENTRADA = "ofertas_filtradas_v2.csv"
ARQUIVO_SAIDA = "top_ofertas_v6.csv"

LIMITE_TOTAL = 50
LIMITE_POR_CATEGORIA = 5


def numero(valor):
    try:
        return float(str(valor).replace(",", "."))
    except (ValueError, TypeError):
        return 0.0


def calcular_pontuacao(produto):
    desconto = numero(produto.get("discount_percentage"))
    avaliacao = numero(produto.get("item_rating"))
    preco = numero(produto.get("sale_price"))

    # ---------------------------------
    # DESCONTO — até 50 pontos
    # ---------------------------------

    desconto_limitado = min(desconto, 90)

    pontos_desconto = (
        desconto_limitado / 90
    ) * 50

    # ---------------------------------
    # AVALIAÇÃO — até 30 pontos
    # ---------------------------------

    pontos_avaliacao = (
        max(0, min(avaliacao, 5)) / 5
    ) * 30

    # ---------------------------------
    # PREÇO — até 20 pontos
    # ---------------------------------

    if preco <= 50:
        pontos_preco = 20
    elif preco <= 100:
        pontos_preco = 18
    elif preco <= 200:
        pontos_preco = 15
    elif preco <= 500:
        pontos_preco = 11
    elif preco <= 1000:
        pontos_preco = 7
    elif preco <= 2000:
        pontos_preco = 4
    else:
        pontos_preco = 2

    return round(
        pontos_desconto
        + pontos_avaliacao
        + pontos_preco,
        2
    )


produtos = []

with open(
    ARQUIVO_ENTRADA,
    encoding="utf-8-sig",
    newline="",
    errors="replace"
) as arquivo:

    leitor = csv.DictReader(arquivo)

    for produto in leitor:

        # Aplica as regras editoriais
        if not produto_permitido(produto):
            continue

        produto["pontuacao"] = calcular_pontuacao(produto)

        produtos.append(produto)


# ---------------------------------
# ORDENAÇÃO
# ---------------------------------

produtos.sort(
    key=lambda x: (
        x["pontuacao"],
        numero(x.get("discount_percentage")),
        numero(x.get("item_rating")),
        -numero(x.get("sale_price"))
    ),
    reverse=True
)


# ---------------------------------
# SELEÇÃO COM DIVERSIDADE
# ---------------------------------

selecionadas = []
categorias = {}


for produto in produtos:

    categoria = (
        produto.get("global_category1", "")
        .strip()
    )

    quantidade = categorias.get(categoria, 0)

    if quantidade >= LIMITE_POR_CATEGORIA:
        continue

    selecionadas.append(produto)

    categorias[categoria] = quantidade + 1

    if len(selecionadas) >= LIMITE_TOTAL:
        break


# ---------------------------------
# GRAVAÇÃO
# ---------------------------------

campos = [
    "itemid",
    "title",
    "price",
    "sale_price",
    "discount_percentage",
    "item_rating",
    "image_link",
    "product_short link",
    "global_category1",
    "global_category2",
    "global_item_attributes",
    "pontuacao"
]


with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8-sig",
    newline=""
) as arquivo:

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=campos
    )

    escritor.writeheader()

    for produto in selecionadas:

        escritor.writerow({
            campo: produto.get(campo, "")
            for campo in campos
        })


print("\n==============================")
print(" RANKING V6 FINALIZADO")
print("==============================")
print(f"Ofertas elegíveis: {len(produtos)}")
print(f"Ofertas selecionadas: {len(selecionadas)}")
print(f"Limite por categoria: {LIMITE_POR_CATEGORIA}")
print(f"Arquivo criado: {ARQUIVO_SAIDA}")
