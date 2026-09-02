import csv
import json

ARQUIVO_ENTRADA = "top_ofertas_v6.csv"
ARQUIVO_SAIDA = "ofertas_shopee.json"

ofertas = []

with open(
    ARQUIVO_ENTRADA,
    encoding="utf-8-sig",
    newline="",
    errors="replace"
) as arquivo:

    leitor = csv.DictReader(arquivo)

    for produto in leitor:

        oferta = {
            "id": f"shopee-{produto['itemid']}",
            "nome": produto["title"].strip(),
	    "loja": "Shopee",
            "categoria": produto["global_category1"].strip(),
            "preco": float(produto["sale_price"]),
            "precoAntigo": float(produto["price"]),
            "comissao": None,
            "imagem": produto["image_link"].strip(),
            "link": produto["product_short link"].strip(),
            "ativo": True
        }

        ofertas.append(oferta)


with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as arquivo:

    json.dump(
        ofertas,
        arquivo,
        ensure_ascii=False,
        indent=2
    )


print("\n==============================")
print(" JSON GERADO")
print("==============================")
print(f"Ofertas convertidas: {len(ofertas)}")
print(f"Arquivo criado: {ARQUIVO_SAIDA}")
