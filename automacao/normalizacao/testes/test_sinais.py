import pytest

from automacao.normalizacao.sinais import criar_sinal


def test_criar_sinal():
    sinal = criar_sinal(
        termo="Perfume",
        origem="title",
        normalizacao="perfume",
        intensidade="forte",
    )

    assert sinal.termo == "Perfume"
    assert sinal.origem == "title"
    assert sinal.normalizacao == "perfume"
    assert sinal.intensidade == "forte"


def test_criar_sinal_limpa_espacos():
    sinal = criar_sinal(
        termo="  perfume  ",
        origem="title",
        normalizacao="  perfume ",
        intensidade="forte",
    )

    assert sinal.termo == "perfume"
    assert sinal.normalizacao == "perfume"


def test_termo_vazio():
    with pytest.raises(ValueError):
        criar_sinal(
            termo="",
            origem="title",
            normalizacao="perfume",
            intensidade="forte",
        )


def test_normalizacao_vazia():
    with pytest.raises(ValueError):
        criar_sinal(
            termo="perfume",
            origem="title",
            normalizacao="",
            intensidade="forte",
        )


def test_extrair_atributos():
    valor = '[{"formatted_value":"Leather"},{"formatted_value":"Unisex"}]'

    from automacao.normalizacao.sinais import extrair_atributos

    resultado = extrair_atributos(valor)

    assert resultado == ["Leather", "Unisex"]


def test_atributos_vazios():
    from automacao.normalizacao.sinais import extrair_atributos

    assert extrair_atributos("") == []


def test_atributos_invalidos():
    from automacao.normalizacao.sinais import extrair_atributos

    assert extrair_atributos("texto inválido") == []


def test_normalizar_termo():
    from automacao.normalizacao.sinais import normalizar_termo

    assert normalizar_termo("  PERFUME  ") == "perfume"
    assert normalizar_termo("Pressão Arterial") == "pressão arterial"
    assert normalizar_termo("") == ""
    assert normalizar_termo(None) == ""


def test_extrair_sinais_fontes_textuais():
    from automacao.normalizacao.sinais import extrair_sinais

    produto = {
        "title": "  Perfume Floral  ",
        "description": "Perfume feminino de 100ml",
        "global_category1": "Beauty",
        "global_category2": "Perfumes",
        "global_item_attributes": "",
    }

    sinais = extrair_sinais(produto)

    assert len(sinais) == 4

    assert sinais[0].termo == "perfume floral"
    assert sinais[0].origem == "title"
    assert sinais[0].intensidade == "forte"

    assert sinais[1].termo == "perfume feminino de 100ml"
    assert sinais[1].origem == "description"
    assert sinais[1].intensidade == "media"


def test_extrair_sinais_com_atributos():
    from automacao.normalizacao.sinais import extrair_sinais

    produto = {
        "title": "Pulseira de couro",
        "global_item_attributes": (
            '[{"formatted_value":"Leather"},'
            '{"formatted_value":"Unisex"}]'
        ),
    }

    sinais = extrair_sinais(produto)

    assert len(sinais) == 3
    assert sinais[2].origem == "global_item_attributes"
    assert sinais[2].normalizacao == "unisex"


def test_extrair_sinais_sem_dados():
    from automacao.normalizacao.sinais import extrair_sinais

    assert extrair_sinais({}) == []
def test_sinal_textual_com_palavra_contextual():
    from automacao.normalizacao.sinais import extrair_sinais

    produto = {
        "title": "Chaveiro de carros",
        "description": "Chaveiro decorativo para presentear",
        "global_category1": "Fashion Accessories",
        "global_category2": "Keychains",
        "global_item_attributes": "",
    }

    sinais = extrair_sinais(produto)

    textos = [sinal.normalizacao for sinal in sinais]

    assert "chaveiro de carros" in textos
    assert "chaveiro decorativo para presentear" in textos
