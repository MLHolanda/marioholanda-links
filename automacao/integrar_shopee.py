import json

ARQUIVO_SITE = "/home/mario/Documentos/marioholanda-links/ofertas.json"
ARQUIVO_SHOPEE = "ofertas_shopee.json"


with open(
    ARQUIVO_SITE,
    "r",
    encoding="utf-8"
) as arquivo:
    ofertas_site = json.load(arquivo)


with open(
    ARQUIVO_SHOPEE,
    "r",
    encoding="utf-8"
) as arquivo:
    ofertas_shopee = json.load(arquivo)


# Remove somente ofertas originadas da Shopee.
# As ofertas das outras plataformas permanecem intactas.
outras_ofertas = [
    oferta
    for oferta in ofertas_site
    if not str(oferta.get("id", "")).startswith("shopee-")
]


# Junta as ofertas das outras plataformas
# com a nova seleção da Shopee.
novo_arquivo = outras_ofertas + ofertas_shopee


# Verifica IDs duplicados antes de gravar.
ids = [
    oferta.get("id")
    for oferta in novo_arquivo
]


if len(ids) != len(set(ids)):
    raise ValueError(
        "ERRO: existem IDs duplicados. "
        "O arquivo original não foi alterado."
    )


# Grava o novo arquivo.
with open(
    ARQUIVO_SITE,
    "w",
    encoding="utf-8"
) as arquivo:

    json.dump(
        novo_arquivo,
        arquivo,
        ensure_ascii=False,
        indent=2
    )


print("\n==============================")
print(" MERGE V2 FINALIZADO")
print("==============================")
print(f"Ofertas no arquivo anterior: {len(ofertas_site)}")
print(f"Novas ofertas Shopee: {len(ofertas_shopee)}")
print(f"Ofertas finais: {len(novo_arquivo)}")
print("Ofertas Shopee antigas substituídas.")
print("Outras plataformas preservadas.")
