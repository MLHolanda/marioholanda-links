from typing import Any


CAMPOS_TEXTO = (
    "itemid",
    "title",
    "description",
    "image_link",
    "product_short link",
    "global_category1",
    "global_category2",
    "global_item_attributes",
)

CAMPOS_NUMERICOS = (
    "price",
    "sale_price",
    "discount_percentage",
    "item_rating",
)


def limpar_texto(valor: Any) -> str:
    """Converte valores textuais para string limpa.

    Valores ausentes ou vazios retornam "".
    """
    if valor is None:
        return ""

    return str(valor).strip()


def converter_numero(valor: Any) -> float | None:
    """Converte um valor para float.

    Valores ausentes, vazios ou inválidos retornam None.
    """
    if valor is None:
        return None

    texto = str(valor).strip()

    if not texto:
        return None

    try:
        return float(texto.replace(",", "."))
    except ValueError:
        return None


def preparar_produto(produto_bruto: dict[str, Any]) -> dict[str, Any]:
    """Prepara um produto bruto para as etapas seguintes.

    Esta função apenas limpa textos e converte campos numéricos.
    Não classifica, não aplica elegibilidade e não faz ranking.
    """
    produto_preparado: dict[str, Any] = {}

    for campo in CAMPOS_TEXTO:
        produto_preparado[campo] = limpar_texto(
            produto_bruto.get(campo)
        )

    for campo in CAMPOS_NUMERICOS:
        produto_preparado[campo] = converter_numero(
            produto_bruto.get(campo)
        )

    return produto_preparado
