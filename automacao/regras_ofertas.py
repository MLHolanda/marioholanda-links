# ==========================================
# REGRAS EDITORIAIS
# MÁRIO HOLANDA OFERTAS
# ==========================================


# Categorias que nunca devem entrar
# automaticamente na vitrine.
CATEGORIAS_BLOQUEADAS = {
    "sexual wellness",
    "medical supplies",
}


# Termos relacionados a produtos adultos,
# médicos ou tratamentos.
TERMOS_BLOQUEADOS = {
    # ------------------------------
    # ADULTOS
    # ------------------------------
    "dildo",
    "vibrador",
    "vibrador feminino",
    "vibrador masculino",
    "masturbador",
    "masturbador masculino",
    "masturbador feminino",
    "sex shop",
    "strap on",
    "plug anal",
    "plug vaginal",
    "algema sexual",
    "bomba peniana",

    # ------------------------------
    # PRODUTOS MÉDICOS
    # ------------------------------
    "inalador",
    "nebulizador",
    "nebulização",
    "esfigmomanômetro",
    "esfigmomanometro",
    "pressão arterial",
    "pressao arterial",
    "medidor de pressão",
    "medidor de pressao",
    "órtese",
    "ortese",
    "tala ortopédica",
    "tala ortopedica",
    "fascite plantar",
    "esporão do calcâneo",
    "esporao do calcaneo",

    # ------------------------------
    # SUPLEMENTOS
    # ------------------------------
    "melatonina",
    "l-triptofano",
    "triptofano",
    "whey protein",
    "suplemento alimentar",
    "suplemento alimentar em pó",
    "suplemento alimentar em po",
}


def produto_permitido(produto):

    categoria1 = (
        produto.get("global_category1", "")
        .strip()
        .lower()
    )

    categoria2 = (
        produto.get("global_category2", "")
        .strip()
        .lower()
    )

    titulo = (
        produto.get("title", "")
        .strip()
        .lower()
    )

    # ------------------------------------------
    # 1. BLOQUEIO POR CATEGORIA
    # ------------------------------------------

    if categoria2 in CATEGORIAS_BLOQUEADAS:
        return False


    # ------------------------------------------
    # 2. BLOQUEIO POR TERMOS NO TÍTULO
    # ------------------------------------------

    texto = f"{titulo} {categoria1} {categoria2}"

    for termo in TERMOS_BLOQUEADOS:

        if termo.lower() in texto:
            return False


    # ------------------------------------------
    # 3. PRODUTO APROVADO
    # ------------------------------------------

    return True
