from automacao.normalizacao.preparador import preparar_produto


def test_produto_normal():
    bruto = {
        "itemid": "123",
        "title": "  Perfume Floral  ",
        "price": "119.90",
        "sale_price": "79.90",
        "discount_percentage": "33",
        "item_rating": "4.8",
    }

    resultado = preparar_produto(bruto)

    assert resultado["itemid"] == "123"
    assert resultado["title"] == "Perfume Floral"
    assert resultado["price"] == 119.90
    assert resultado["sale_price"] == 79.90
    assert resultado["discount_percentage"] == 33.0
    assert resultado["item_rating"] == 4.8


def test_avaliacao_vazia():
    bruto = {
        "item_rating": "",
    }

    resultado = preparar_produto(bruto)

    assert resultado["item_rating"] is None


def test_preco_invalido():
    bruto = {
        "sale_price": "abc",
    }

    resultado = preparar_produto(bruto)

    assert resultado["sale_price"] is None


def test_numero_com_virgula():
    bruto = {
        "price": "249,90",
        "sale_price": "199,50",
        "discount_percentage": "20",
        "item_rating": "4,5",
    }

    resultado = preparar_produto(bruto)

    assert resultado["price"] == 249.90
    assert resultado["sale_price"] == 199.50
    assert resultado["discount_percentage"] == 20.0
    assert resultado["item_rating"] == 4.5


def test_campos_ausentes():
    resultado = preparar_produto({})

    assert resultado["title"] == ""
    assert resultado["description"] == ""
    assert resultado["image_link"] == ""
    assert resultado["price"] is None
    assert resultado["sale_price"] is None
    assert resultado["discount_percentage"] is None
    assert resultado["item_rating"] is None


def test_texto_com_espacos():
    bruto = {
        "itemid": " 123 ",
        "title": "  Produto de teste  ",
        "global_category1": "  Beauty  ",
    }

    resultado = preparar_produto(bruto)

    assert resultado["itemid"] == "123"
    assert resultado["title"] == "Produto de teste"
    assert resultado["global_category1"] == "Beauty"
