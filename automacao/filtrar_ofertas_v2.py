import csv

ARQUIVO_ENTRADA = "shopee-feed.csv"
ARQUIVO_SAIDA = "ofertas_filtradas_v2.csv"

total_produtos = 0
ofertas_encontradas = 0


def numero(valor):
    try:
        return float(str(valor).replace(",", "."))
    except (ValueError, TypeError):
        return 0


with open(
    ARQUIVO_ENTRADA,
    encoding="utf-8-sig",
    newline="",
    errors="replace"
) as arquivo:

    linhas = (
        linha.replace("\x00", "")
        for linha in arquivo
    )

    leitor = csv.DictReader(linhas)

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
        "global_item_attributes"
    ]

    with open(
        ARQUIVO_SAIDA,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as saida:

        escritor = csv.DictWriter(
            saida,
            fieldnames=campos
        )

        escritor.writeheader()

        for produto in leitor:

            total_produtos += 1

            desconto = numero(
                produto.get("discount_percentage")
            )

            preco_venda = numero(
                produto.get("sale_price")
            )

            avaliacao = numero(
                produto.get("item_rating")
            )

            imagem = produto.get(
                "image_link",
                ""
            )

            link = produto.get(
                "product_short link",
                ""
            )

            if (
                desconto >= 20
                and 20 <= preco_venda <= 5000
                and avaliacao >= 4.5
                and imagem
                and link
            ):

                escritor.writerow({
                    campo: produto.get(campo, "")
                    for campo in campos
                })

                ofertas_encontradas += 1


print("\n==============================")
print(" FILTRO V2 FINALIZADO")
print("==============================")
print(f"Produtos analisados: {total_produtos}")
print(f"Ofertas encontradas: {ofertas_encontradas}")
print(f"\nArquivo criado: {ARQUIVO_SAIDA}")
