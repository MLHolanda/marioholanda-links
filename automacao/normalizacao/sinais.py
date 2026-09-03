from dataclasses import dataclass
from typing import Literal


OrigemSinal = Literal[
    "title",
    "description",
    "global_category1",
    "global_category2",
    "global_item_attributes",
]

IntensidadeSinal = Literal[
    "forte",
    "media",
    "fraca",
]


@dataclass(frozen=True)
class Sinal:
    """Representa uma evidência extraída de um produto."""

    termo: str
    origem: OrigemSinal
    normalizacao: str
    intensidade: IntensidadeSinal


def criar_sinal(
    termo: str,
    origem: OrigemSinal,
    normalizacao: str,
    intensidade: IntensidadeSinal,
) -> Sinal:
    """Cria um sinal validado."""

    termo_limpo = termo.strip()
    normalizacao_limpa = normalizacao.strip()

    if not termo_limpo:
        raise ValueError("termo do sinal não pode ser vazio")

    if not normalizacao_limpa:
        raise ValueError("normalização do sinal não pode ser vazia")

    return Sinal(
        termo=termo_limpo,
        origem=origem,
        normalizacao=normalizacao_limpa,
        intensidade=intensidade,
    )


def extrair_atributos(valor: str) -> list[str]:
    """Extrai valores textuais dos atributos estruturados da Shopee.

    JSON ausente, vazio ou inválido resulta em lista vazia.
    """
    import json

    if not valor or not valor.strip():
        return []

    try:
        dados = json.loads(valor)
    except (json.JSONDecodeError, TypeError):
        return []

    if not isinstance(dados, list):
        return []

    resultados = []

    for item in dados:
        if not isinstance(item, dict):
            continue

        valor_formatado = item.get("formatted_value")

        if valor_formatado is None:
            continue

        valor_formatado = str(valor_formatado).strip()

        if valor_formatado:
            resultados.append(valor_formatado)

    return resultados


def normalizar_termo(valor: str) -> str:
    """Normaliza um termo para comparação sem alterar seus acentos."""
    if valor is None:
        return ""

    return str(valor).strip().lower()


def extrair_sinais(produto: dict) -> list[Sinal]:
    """Extrai sinais básicos das fontes disponíveis do produto."""
    sinais = []

    fontes = (
        ("title", "forte"),
        ("description", "media"),
        ("global_category1", "fraca"),
        ("global_category2", "media"),
    )

    for campo, intensidade in fontes:
        valor = normalizar_termo(produto.get(campo, ""))

        if not valor:
            continue

        sinais.append(
            criar_sinal(
                termo=valor,
                origem=campo,
                normalizacao=valor,
                intensidade=intensidade,
            )
        )

    for atributo in extrair_atributos(produto.get("global_item_attributes", "")):
        valor = normalizar_termo(atributo)

        if not valor:
            continue

        sinais.append(
            criar_sinal(
                termo=atributo,
                origem="global_item_attributes",
                normalizacao=valor,
                intensidade="fraca",
            )
        )

    return sinais
