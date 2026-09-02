# CONTRATO DO NORMALIZADOR — V1

## 1. Objetivo

Definir o contrato técnico das etapas de preparação e normalização dos produtos recebidos dos feeds de afiliados.

O normalizador transforma dados brutos de uma fonte em uma estrutura padronizada que poderá ser usada pelas etapas posteriores de elegibilidade, ranking, seleção, estado e publicação.

O normalizador não publica ofertas, não escolhe as melhores ofertas e não substitui as regras de elegibilidade.

---

## 2. Fluxo

```text
ProdutoBruto
    ↓
Preparador
    ↓
ProdutoPreparado
    ↓
Classificador / Normalizador
    ↓
ProdutoNormalizado
```

Responsabilidades:

- ProdutoBruto: representar os dados recebidos da fonte.
- Preparador: limpar e converter os dados para tipos consistentes.
- Normalizador: interpretar a natureza do produto e convertê-lo para o modelo padrão do projeto.
- Elegibilidade: decidir se o produto pode participar da vitrine.
- Ranking: calcular a prioridade entre produtos elegíveis.
- Seleção: escolher quais ofertas formarão a vitrine.
- Publicação: atualizar o arquivo público somente após todas as validações.

---

# 3. ProdutoBruto

## 3.1 Conceito

ProdutoBruto representa o registro exatamente como recebido do feed de origem.

Nenhuma interpretação de negócio deve ser aplicada nessa etapa.

Para a Shopee, o feed atualmente utilizado possui os seguintes campos:

```text
image_link
itemid
price
global_category1
description
global_category2
global_item_attributes
item_rating
sale_price
global_catid2
discount_percentage
image_link_3
title
global_catid1
product_link
product_short link
```

## 3.2 Regra

O conteúdo recebido da fonte deve ser preservado durante a entrada do pipeline, permitindo auditoria e diagnóstico.

---

# 4. ProdutoPreparado

## 4.1 Objetivo

ProdutoPreparado representa o mesmo produto após limpeza técnica e conversão para tipos consistentes.

Esta etapa não decide a categoria pública definitiva e não decide a elegibilidade.

## 4.2 Campos mínimos

| Campo | Tipo | Fonte | Transformação |
|---|---|---|---|
| itemid | string | itemid | limpar espaços |
| title | string | title | limpar espaços |
| description | string | description | limpar espaços |
| price | number/null | price | converter para número |
| sale_price | number/null | sale_price | converter para número |
| discount_percentage | number/null | discount_percentage | converter para número |
| item_rating | number/null | item_rating | converter para número |
| image_link | string | image_link | limpar espaços |
| product_short link | string | product_short link | limpar espaços |
| global_category1 | string | global_category1 | limpar espaços |
| global_category2 | string | global_category2 | limpar espaços |
| global_item_attributes | string | global_item_attributes | limpar espaços |

## 4.3 Campos auxiliares

Os seguintes campos continuam disponíveis como dados da fonte quando necessários:

```text
global_catid1
global_catid2
image_link_3
product_link
```

Eles não fazem parte do contrato mínimo do ProdutoPreparado.

## 4.4 Regras de conversão

### Campos textuais

Valores ausentes ou vazios:

```text
""
```

Exemplo:

```text
"  Perfume Floral  " → "Perfume Floral"
```

A limpeza não deve alterar o significado do texto.

### Campos numéricos

Valores válidos devem ser convertidos para número.

Exemplos:

```text
"249.90" → 249.90
"4.8"    → 4.8
```

Valores ausentes ou inválidos:

```text
null
```

Exemplo:

```text
""    → null
"abc" → null
```

null significa ausência de dado válido e não significa valor zero.

---

# 5. ProdutoNormalizado

## 5.1 Objetivo

ProdutoNormalizado representa o produto segundo o contrato permanente do Mário Holanda Ofertas.

O modelo V1 possui 14 campos:

### Regras de integridade de preço

- `preco` deve ser um valor numérico positivo para que o produto avance às etapas seguintes;
- `precoAntigo` pode ser `null` quando o valor da fonte não for confiável;
- `precoAntigo` nunca deve ser inventado ou calculado simplesmente a partir do desconto;
- `null` não deve ser convertido automaticamente em zero.

```text
id
loja
nome
categoria
preco
precoAntigo
desconto
avaliacao
imagem
link
ativo
comissao
dataAtualizacao
validadeAte
```

## 5.2 Mapeamento inicial para Shopee

### Regra de categoria

O campo `categoria` armazenará o caminho canônico da taxonomia pública. Quando houver subcategoria, será usado o formato:

```text
Categoria > Subcategoria
```

Exemplo:

```text
Casa & Jardim > Decoração
```

Quando uma categoria não possuir subcategoria definida para aquele produto, será usado apenas o nome da categoria.

| Campo normalizado | Origem / regra |
|---|---|
| id | `shopee-{itemid}` |
| loja | `"Shopee"` |
| nome | `title` limpo |
| categoria | caminho canônico da taxonomia pública, no formato `Categoria > Subcategoria` quando houver subcategoria |
| preco | `sale_price`, desde que seja numérico e positivo |
| precoAntigo | `price`, somente quando confiável; nunca inventar ou calcular a partir do desconto |
| desconto | `discount_percentage` ou cálculo quando necessário |
| avaliacao | `item_rating` |
| imagem | `image_link` |
| link | `product_short link` |
| ativo | não é definido pelo normalizador; será definido posteriormente pela etapa de estado/elegibilidade |
| comissao | opcional |
| dataAtualizacao | data/hora da atualização |
| validadeAte | validade real disponível para a oferta |

---

# 6. Responsabilidades do normalizador

O normalizador é responsável por:

- interpretar a natureza do produto;
- identificar categoria e subcategoria segundo a taxonomia do projeto;
- usar sinais provenientes de título, descrição, categoria de origem e atributos;
- resolver conflitos entre sinais;
- produzir uma classificação determinística quando houver evidência suficiente;
- produzir metadado interno de confiança quando aplicável; esse metadado não faz parte dos 14 campos publicados;
- retornar produto não classificado quando a evidência for insuficiente.

---

# 7. O que NÃO pertence ao normalizador

O normalizador não deve:

- decidir se uma oferta pode aparecer na vitrine;
- aplicar o ranking final;
- selecionar as 50 ofertas;
- publicar `ofertas.json`;
- substituir uma oferta existente;
- controlar o histórico;
- decidir comissão;
- inventar preços;
- inventar validade;
- inventar categoria quando não houver evidência suficiente.

---

# 8. Ausência de informação

A ausência de um dado não deve ser convertida automaticamente em um valor artificial.

Exemplos:

```text
avaliação ausente → null
preço inválido → null
preço antigo não confiável → null
comissão ausente → null
```

Esses valores serão tratados pelas etapas responsáveis pelas respectivas decisões.

---

# 9. Classificação

A classificação deve utilizar evidência contextual.

Não é permitido classificar um produto com base em uma palavra isolada quando o contexto indicar outro significado.

Exemplo conceitual:

```text
"chaveiro de carros"
```

não deve ser classificado como peça ou acessório automotivo apenas porque contém a palavra "carros".

A decisão deve considerar o conjunto de sinais.

---

# 10. Confiança

A classificação poderá utilizar três níveis:

```text
alta
média
baixa
```

Regra geral V1:

- alta: identificação clara;
- média: evidência suficiente, mas com alguma ambiguidade;
- baixa: evidência insuficiente.

Classificações de baixa confiança não devem ser publicadas automaticamente sem tratamento posterior.

---

# 11. Exemplos

## Exemplo 1 — produto normal

Entrada:

```text
itemid = 123
title = "Perfume Floral Feminino 100ml"
sale_price = "79.90"
price = "119.90"
item_rating = "4.8"
discount_percentage = "33"
```

Saída parcial esperada:

```text
id = "shopee-123"
loja = "Shopee"
nome = "Perfume Floral Feminino 100ml"
preco = 79.90
precoAntigo = 119.90
desconto = 33
avaliacao = 4.8
```

A categoria pública deverá ser definida pelo classificador segundo a taxonomia V1, usando o caminho canônico `Categoria > Subcategoria` quando houver subcategoria.

## Exemplo 2 — avaliação ausente

Entrada:

```text
item_rating = ""
```

Após preparação:

```text
item_rating = null
```

Isso não significa avaliação zero.

A elegibilidade decidirá posteriormente se o produto pode participar da seleção normal.

## Exemplo 3 — preço inválido

Entrada:

```text
sale_price = "abc"
```

Após preparação:

```text
sale_price = null
```

O produto não deve receber um preço artificial.

---

# 12. Princípio de separação

O mesmo produto deve passar por etapas independentes:

```text
Preparar dados
    ↓
Normalizar significado
    ↓
Verificar elegibilidade
    ↓
Calcular ranking
    ↓
Selecionar
    ↓
Controlar estado
    ↓
Publicar
```

Cada etapa deve possuir responsabilidade única e ser testável isoladamente.

---

# 13. Regra de evolução

O contrato V1 deve ser suficientemente genérico para receber outras fontes além da Shopee.

A fonte pode mudar.

O contrato normalizado deve permanecer estável.

Portanto:

```text
Feed Shopee ─┐
Feed Amazon ─┤
Feed Magalu ─┼──→ Normalização ─→ Modelo padrão
Feed ML ─────┤
Outros ──────┘
```

A identidade visual, regras específicas de loja e publicação do Mário Holanda devem permanecer separadas do motor de normalização.

---

# 14. Status

Documento de trabalho — V1.

Este contrato será revisado antes da implementação do código.
