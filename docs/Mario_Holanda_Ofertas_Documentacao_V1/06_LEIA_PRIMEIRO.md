# Mário Holanda Ofertas — Leia Primeiro

## O projeto em uma página

O **Mário Holanda Ofertas** é um motor de curadoria e publicação automática de ofertas afiliadas.

### Objetivo

Receber produtos de parceiros, transformar os dados para uma linguagem própria, eliminar ofertas inadequadas, ranquear as melhores e publicar uma vitrine pública estável.

### Fluxo

```text
FEED
 ↓
VALIDAÇÃO
 ↓
NORMALIZAÇÃO
 ↓
ELEGIBILIDADE
 ↓
RANKING
 ↓
SELEÇÃO
 ↓
ESTADO/HISTÓRICO
 ↓
VALIDAÇÃO FINAL
 ↓
ofertas.json
 ↓
PUBLICAÇÃO
```

### Regra central

> **Nunca forçar uma classificação e nunca publicar uma oferta que não tenha passado pelas regras de elegibilidade e validação.**

### Modelo da oferta

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

### Ranking

Desconto + avaliação + preço, com desempate por:

1. maior desconto;
2. menor preço;
3. maior avaliação.

### Limite

Até 50 ofertas, com distribuição máxima de 10 por loja para Drogasmil, Amazon, Mercado Livre e Magalu; Shopee preenche as posições restantes.

### Segurança

Falha crítica → não publicar nova versão → manter última versão válida.

### Evolução

Taxonomia, elegibilidade e ranking devem ser configuráveis e refináveis.

### Para IA codadora

Ler este arquivo primeiro e depois o Documento Mestre e os documentos específicos da etapa.
