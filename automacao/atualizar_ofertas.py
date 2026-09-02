import subprocess
import sys


ETAPAS = [
    "baixar_feed.py",
    "filtrar_ofertas_v2.py",
    "ranking_ofertas_v6.py",
    "gerar_ofertas_json.py",
    "integrar_shopee.py"
]


print("\n==============================")
print(" MÁRIO HOLANDA OFERTAS")
print(" ATUALIZAÇÃO AUTOMÁTICA")
print("==============================\n")


for etapa in ETAPAS:

    print(f"\n>>> Executando: {etapa}")

    resultado = subprocess.run(
        [sys.executable, etapa]
    )

    if resultado.returncode != 0:

        print("\nERRO!")
        print(f"A etapa {etapa} falhou.")
        print("Processo interrompido.")

        sys.exit(1)


print("\n==============================")
print(" ATUALIZAÇÃO CONCLUÍDA")
print("==============================")
print("Todas as etapas foram executadas.")
