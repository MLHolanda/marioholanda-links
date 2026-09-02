# Mário Holanda Ofertas — Regras de Elegibilidade V1

## 1. Objetivo

Determinar se um produto classificado pode ou não participar da vitrine pública.

A elegibilidade é uma etapa separada da classificação.

## 2. Regra geral

```text
Produto recebido
   ↓
Estruturalmente válido?
   ↓ sim
Classificável?
   ↓ sim
Elegível?
   ↓ sim
Participa do ranking
```

## 3. Requisitos básicos de dados

### Imagem

Obrigatória e válida.

Sem imagem válida:

```text
não elegível para a vitrine
```

Não substituir automaticamente por imagem genérica.

### Link

Obrigatório, válido e relacionado à loja correta.

Quando houver rastreamento afiliado, preservá-lo conforme o contrato da fonte.

### Avaliação

Quando a regra de seleção exigir avaliação válida, ofertas sem avaliação confiável ficam fora da seleção normal.

Nunca inventar avaliação.

### Preço

Deve existir valor atual confiável dentro das regras de seleção.

### Desconto

Deve ser confiável conforme a fonte ou cálculo baseado em preços confiáveis.

Nunca inventar desconto.

## 4. Validade

- validade explicitamente informada pelo parceiro deve ser respeitada;
- duração pode ser convertida em data/hora;
- ausência ou invalidade da validade não cria uma data falsa;
- na ausência de validade confiável, aplicar a referência de segurança operacional do projeto;
- oferta expirada não deve ficar ativa.

## 5. Álcool

Produtos de bebidas alcoólicas são **inelegíveis para a vitrine**.

Exemplo identificado durante a análise:

```text
Cachaça
→ categoria pode ser Bebidas
→ elegibilidade = NÃO
```

## 6. Saúde

A categoria contém, entre outros:

- suplementos;
- materiais médicos;
- equipamentos;
- cuidados pessoais;
- bem-estar íntimo.

### Política V1 aprovada

Na V1, os seguintes grupos são **inelegíveis para a vitrine pública**:

- suplementos;
- equipamentos e materiais médicos;
- produtos classificados como `Sexual Wellness`.

Cuidados pessoais de natureza cosmética ou de higiene que possam ser classificados com segurança fora do universo de tratamento médico podem ser direcionados para `Beleza & Cuidados` e seguir as regras gerais.

A regra deliberadamente conservadora poderá ser revisada em versão futura, sem alteração estrutural do motor.

## 7. Saúde veterinária

Produtos classificados em `Pets → Cuidados de Saúde` são **inelegíveis na V1**.

A classificação pode ser mantida internamente para fins de diagnóstico e histórico, mas esses produtos não participam da seleção pública. Uma política mais abrangente poderá ser definida em versão futura mediante revisão formal.

## 8. Produtos sem classificação confiável

Regra aprovada:

```text
classificação confiável = não
→ não publicar
```

A ausência de classificação não deve ser resolvida com `Outros` apenas para preencher espaço.

## 9. Produtos desaparecidos

Quando um produto deixa de aparecer no feed:

- retirar da vitrine imediatamente;
- manter registro interno quando aplicável;
- reativar quando retornar e estiver elegível;
- após dois ciclos consecutivos ausente, permanecer inativo até retorno.

## 10. Produtos que ficam inelegíveis

Se continuarem no feed, mas deixarem de atender às regras:

- retirar da vitrine imediatamente;
- manter registro interno quando aplicável;
- permitir retorno quando voltarem a ser elegíveis.

## 11. Regra de segurança

Em caso de dúvida relevante:

> **não publicar**.

A estratégia V1 privilegia confiabilidade sobre preenchimento máximo da vitrine.
