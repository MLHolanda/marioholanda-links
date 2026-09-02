# Mário Holanda Ofertas — Estratégia de Escala e Reutilização por Afiliados

## 1. Objetivo

Preparar o projeto para que a experiência Mário Holanda possa evoluir, no futuro, para um motor reutilizável por outros afiliados sem comprometer a identidade do projeto original.

Não existe garantia de viralização. O objetivo técnico é criar uma base **compartilhável, confiável, modular e demonstrável**.

## 2. O que torna o projeto compartilhável

### Motor independente

O núcleo não deve depender do nome Mário Holanda para funcionar.

### Configuração por perfil

Um futuro afiliado poderá ter configuração própria para:

- nome/marca;
- lojas permitidas;
- limites por loja;
- taxonomia pública;
- regras específicas de elegibilidade;
- identidade visual;
- parâmetros de ranking;
- tracking de afiliado.

### Adaptadores de parceiros

Cada parceiro pode ter um adaptador responsável por converter seu feed para o formato interno.

```text
Shopee adapter ─┐
Amazon adapter ─┤
Mercado Livre ──┤→ Modelo interno de oferta
Magalu adapter ─┤
Drogasmil ──────┘
```

## 3. Modelo de produto

O motor pode ser pensado como uma plataforma de seleção e publicação de ofertas, enquanto cada afiliado possui uma camada de configuração.

```text
                MOTOR
                  │
       ┌──────────┼──────────┐
       │          │          │
   Afiliado A  Afiliado B  Mário Holanda
```

A V1 não precisa implementar multi-tenant completo. Basta não criar acoplamentos que impeçam essa evolução.

## 4. O que deve ser demonstrável publicamente

Para aumentar credibilidade perante outros afiliados, o projeto deve futuramente conseguir demonstrar, sem expor segredos:

- atualização automática;
- seleção de boas ofertas;
- rastreabilidade das regras;
- estabilidade do feed público;
- tratamento de falhas;
- histórico de evolução;
- documentação clara.

## 5. O que não deve ser compartilhado

Nunca publicar:

- URLs privadas de feeds;
- tokens e secrets;
- credenciais de parceiros;
- dados internos não destinados ao público;
- detalhes de configuração que comprometam contas afiliadas.

## 6. Posicionamento futuro

Quando a V1 estiver comprovadamente estável, o projeto poderá ser apresentado como referência de uma arquitetura de automação de ofertas, e não apenas como uma página de links.

A ordem correta é:

```text
produto funcionando
→ confiabilidade
→ métricas
→ casos reais
→ documentação
→ apresentação externa
```

Não devemos inverter essa ordem.

## 7. Evolução futura possível

- painel administrativo;
- cadastro simplificado de novos parceiros;
- configuração de novos afiliados;
- observabilidade;
- métricas de CTR/conversão;
- regras personalizadas por perfil;
- versionamento de taxonomias;
- experimentação de ranking;
- geração de feeds públicos diferentes a partir do mesmo núcleo.

Esses itens são possibilidades pós-V1, não requisitos obrigatórios da primeira implementação.
