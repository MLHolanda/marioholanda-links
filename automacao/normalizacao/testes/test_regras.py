from automacao.normalizacao.regras import RegraClassificacao


def test_criar_regra_com_subcategoria():
    regra = RegraClassificacao(
        id="N001",
        prioridade=100,
        categoria="VEICULOS",
        subcategoria="PECAS_CARROS",
        inclui=("bateria",),
        apoios=("automotivo", "12v"),
        exclui=("brinquedo",),
    )

    assert regra.id == "N001"
    assert regra.prioridade == 100
    assert regra.categoria == "VEICULOS"
    assert regra.subcategoria == "PECAS_CARROS"
    assert regra.inclui == ("bateria",)
    assert regra.apoios == ("automotivo", "12v")
    assert regra.exclui == ("brinquedo",)


def test_regra_pode_nao_ter_subcategoria():
    regra = RegraClassificacao(
        id="N002",
        prioridade=200,
        categoria="PRESENTES_PERSONALIZADOS",
        subcategoria=None,
    )

    assert regra.subcategoria is None
    assert regra.inclui == ()
    assert regra.apoios == ()
    assert regra.exclui == ()
