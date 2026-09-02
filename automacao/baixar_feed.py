import os
import urllib.request


ARQUIVO_ENV = ".env"
ARQUIVO_FEED = "shopee-feed.csv"


def carregar_url():
    with open(ARQUIVO_ENV, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha.startswith("SHOPEE_FEED_URL="):
                return linha.split("=", 1)[1].strip()

    return None


url = carregar_url()

if not url:
    print("ERRO: SHOPEE_FEED_URL não encontrada no .env")
    raise SystemExit(1)


print("\n==============================")
print(" DOWNLOAD DO FEED SHOPEE")
print("==============================")
print("Iniciando download...")


try:
    urllib.request.urlretrieve(url, ARQUIVO_FEED)

    tamanho = os.path.getsize(ARQUIVO_FEED)
    tamanho_mb = tamanho / (1024 * 1024)

    print("\nDownload concluído com sucesso!")
    print(f"Arquivo: {ARQUIVO_FEED}")
    print(f"Tamanho: {tamanho_mb:.2f} MB")

except Exception as erro:
    print("\nERRO durante o download:")
    print(type(erro).__name__)
    raise SystemExit(1)
