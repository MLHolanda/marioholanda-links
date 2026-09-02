# Mário Holanda Ofertas — Documento Mestre V1

**Status:** Em consolidação técnica antes da implementação do normalizador  
**Versão:** 1.0 — base de trabalho  
**Objetivo:** servir como fonte de verdade do projeto para Mário, Athena e futuras IAs codadoras.

---

## 1. Propósito do documento

Este documento reúne a visão, os princípios, as regras e as decisões necessárias para transformar o **Mário Holanda Ofertas** em um motor confiável de ofertas afiliadas.

Ele deve permitir que uma nova pessoa ou IA entenda o projeto sem depender da memória desta conversa.

### Regra de ouro

> **A documentação é o contrato do projeto. O código deve obedecer à documentação; quando o código precisar de uma mudança de comportamento, a documentação deve ser atualizada junto.**

---

## 2. Visão do produto

O Mário Holanda Ofertas é uma plataforma de ofertas e cupons baseada em links de afiliados, cujo núcleo deverá:

1. receber dados de produtos de parceiros;
2. validar a integridade dos dados;
3. normalizar produtos para uma linguagem interna própria;
4. aplicar regras de elegibilidade;
5. selecionar ofertas de maior qualidade;
6. manter estado e histórico sem duplicações;
7. gerar uma versão pública estável de `ofertas.json`;
8. publicar automaticamente somente quando todas as validações forem aprovadas.

A experiência pública pertence à identidade **Mário Holanda**. O motor deve, entretanto, ser construído de forma modular, configurável e desacoplada da identidade visual/comercial, permitindo futura adaptação a outros afiliados sem reconstrução do núcleo.

---

## 3. Visão de longo prazo

O projeto V1 deve resolver o problema atual de forma simples e confiável. A arquitetura deve, ao mesmo tempo, permitir evolução posterior.

A estratégia é:

```text
V1 confiável
    ↓
observação em produção
    ↓
medição dos casos reais
    ↓
refinamento de regras
    ↓
V2 / V3 / ...
```

Não é objetivo da V1 prever todos os futuros cenários.

É objetivo da V1 evitar decisões irreversíveis ou acoplamentos que tornem futuras melhorias caras.

---

## 4. Princípios do projeto

### 4.1 Confiabilidade antes de volume

É preferível publicar menos ofertas corretas do que preencher a vitrine com produtos inadequados.

### 4.2 Qualidade antes de quantidade

O limite operacional da vitrine é de até 50 ofertas. Não existe obrigação de preencher 50 se não houver 50 ofertas elegíveis.

### 4.3 Não forçar classificação

Quando o sistema não tiver segurança suficiente para classificar um produto, ele não deve inventar a categoria.

### 4.4 Classificação não é elegibilidade

Um produto pode ser corretamente classificado e ainda assim não poder participar da vitrine.

### 4.5 A origem é sinal, não verdade

Categorias e subcategorias dos parceiros são insumos para classificação, não a taxonomia final do Mário Holanda.

### 4.6 Dados atuais substituem estados antigos

Se preço, desconto ou disponibilidade mudarem, a oferta deve refletir a realidade atual. Não se deve preservar um estado antigo apenas porque ele era mais atraente.

### 4.7 Falha não publica

Em falha crítica da automação, o processo deve parar e não substituir a última versão pública válida.

### 4.8 Segurança por padrão

Segredos, tokens e URLs privadas nunca devem entrar no repositório nem na documentação pública.

### 4.9 Configuração separada de identidade

O motor de ofertas deve separar:

- regras do motor;
- fontes/parceiros;
- identidade da marca/site;
- configurações comerciais.

Essa separação é essencial para a futura reutilização por outros afiliados.

---

## 5. Fluxo macro da automação

```text
Fonte / Parceiro
      ↓
Aquisição do feed
      ↓
Validação estrutural
      ↓
Normalização
      ↓
Elegibilidade
      ↓
Ranking
      ↓
Seleção / distribuição por loja
      ↓
Atualização de estado + histórico
      ↓
Validação final
      ↓
Geração de ofertas.json
      ↓
Publicação
      ↓
Relatório da execução
```

Nenhuma etapa posterior deve mascarar uma falha anterior.

---

## 6. Limite de responsabilidade das etapas

### Aquisição
Responsável por obter o dado mais recente do parceiro.

### Validação estrutural
Responsável por detectar feed ausente, cabeçalho inválido, colunas inesperadas, registros corrompidos e inconsistências graves.

### Normalização
Responsável por transformar a linguagem do parceiro na linguagem interna do projeto.

### Elegibilidade
Responsável por decidir se o produto pode participar da vitrine.

### Ranking
Responsável por estimar qualidade relativa das ofertas elegíveis.

### Estado e histórico
Responsáveis por preservar continuidade, evitar duplicidade e registrar mudanças relevantes.

### Publicação
Responsável somente por disponibilizar uma versão que passou por todas as validações anteriores.

---

## 7. Fonte de verdade dos dados públicos

A vitrine pública deve consumir apenas uma representação normalizada e validada.

O arquivo `ofertas.json` é o artefato público final da seleção.

A fonte bruta do parceiro e arquivos intermediários não devem ser tratados como fonte pública.

---

## 8. Modelo permanente da oferta

Campos aprovados para o modelo permanente:

| Campo | Regra |
|---|---|
| `id` | Identificador estável; combinação de loja + identificador original quando aplicável. Ex.: `shopee-123456789`. |
| `loja` | Valor padronizado: `Shopee`, `Amazon`, `Mercado Livre`, `Magalu`, `Drogasmil`. |
| `nome` | Título original com apenas trim de espaços nas extremidades. |
| `categoria` | Categoria da taxonomia Mário Holanda. |
| `preco` | Valor numérico atual. |
| `precoAntigo` | Opcional; `null` se não houver preço anterior confiável. Nunca inventar. |
| `desconto` | Percentual numérico; usar valor do parceiro quando confiável, caso contrário calcular quando houver preços confiáveis. |
| `avaliacao` | 0–5 ou `null`; nunca inventar. |
| `imagem` | Obrigatória; deve ser válida e proveniente do parceiro. Sem imagem, não entra na vitrine. |
| `link` | Obrigatório; válido e correspondente à loja, preservando rastreamento de afiliado quando aplicável. |
| `ativo` | Booleano; controla atividade atual. |
| `comissao` | Opcional; `null` quando indisponível. Não é critério atual de qualidade. |
| `dataAtualizacao` | Data/hora padronizada da última atualização/processamento. |
| `validadeAte` | Data/hora de expiração conhecida ou limite de segurança definido pelas regras. |

`pontuacao` é temporária do processo de ranking e **não faz parte do modelo permanente atual**.

---

## 9. Regras de identidade e atualização

### 9.1 Mesmo ID = mesma oferta

Se o mesmo `id` reaparecer, o sistema atualiza o registro existente. Não cria duplicata.

### 9.2 Oferta melhorou

Atualizar para o estado atual.

### 9.3 Oferta piorou

Atualizar para a realidade atual. Nunca manter preço/desconto antigo apenas para conservar aparência de promoção.

### 9.4 Oferta desapareceu do feed

- retirar imediatamente da vitrine;
- manter registro interno quando aplicável;
- se voltar, reativar;
- após dois ciclos consecutivos ausente, permanecer inativa até retorno.

### 9.5 Oferta ficou inelegível

Retirar imediatamente da vitrine, mantendo registro interno quando aplicável.

### 9.6 Histórico

O histórico fica separado de `ofertas.json` e registra mudanças relevantes, como:

- alteração de preço;
- alteração de desconto;
- entrada na vitrine;
- saída da vitrine;
- retorno à vitrine;
- outras mudanças relevantes futuras.

---

## 10. Política de elegibilidade V1 — resumo

A V1 adota uma postura conservadora. Classificação correta não implica elegibilidade.

São excluídos da vitrine pública, entre outros casos: bebidas alcoólicas; produtos sem imagem ou link válidos; produtos sem classificação confiável; suplementos; equipamentos e materiais médicos; `Sexual Wellness`; e `Pets → Cuidados de Saúde`.

Alimentos comuns podem participar desde que válidos e aprovados pelas demais regras.

A política pode evoluir em versões futuras sem exigir reconstrução do motor, desde que as regras permaneçam centralizadas e versionadas.

## 10. Regras de falha e publicação

Se ocorrer uma falha crítica:

```text
interromper
    ↓
não gerar/publicar nova versão pública
    ↓
manter última versão pública válida
    ↓
registrar falha
    ↓
produzir relatório da execução
```

A última versão pública válida deve continuar servindo o site.

---

## 11. Relatório obrigatório de execução

Cada ciclo deve produzir uma visão operacional contendo, no mínimo:

- sucesso/falha geral;
- quantidade recebida;
- quantidade elegível;
- quantidade selecionada;
- status de atualização do JSON;
- status de publicação;
- etapa da falha, quando houver;
- motivo da falha.

---

## 12. Estratégia de atualização

A frequência deve respeitar a validade restante das ofertas e o risco de desatualização.

Regras já definidas:

- se houver oferta com validade curta, priorizar verificações frequentes;
- se todas as ofertas tiverem validade longa, é possível reduzir a frequência;
- quando não houver validade conhecida, aplicar a verificação de segurança definida pelo projeto, atualmente limitada a 24h como referência máxima;
- validade é referência de atualização, não garantia de que a oferta continuará disponível até a hora calculada.

---

## 13. Distribuição por loja

A vitrine pode ter até 50 ofertas.

Limites aprovados:

- até 10 Drogasmil;
- até 10 Amazon;
- até 10 Mercado Livre;
- até 10 Magalu;
- Shopee ocupa as posições restantes;
- somente ofertas elegíveis participam;
- se houver menos de 50 elegíveis, publicar menos.

Quando uma loja tiver mais de 10 elegíveis, selecionar as melhores 10 segundo as regras de ranking.

A distribuição não deve ser tratada como promessa matemática de presença de cada loja; ela é uma política de seleção.

---

## 14. Ranking V1

Regras aprovadas:

### Desconto

90% de desconto = 50 pontos máximos.

### Avaliação

5,0 = 30 pontos máximos.  4,5 = 27 pontos.

### Preço

- até R$ 50 → 20 pontos;
- até R$ 100 → 18 pontos;
- até R$ 200 → 15 pontos;
- até R$ 500 → 11 pontos;
- até R$ 1.000 → 7 pontos;
- até R$ 2.000 → 4 pontos;
- acima de R$ 2.000 → 2 pontos.

### Desempate

Ordem desejada:

1. maior desconto;
2. menor preço;
3. maior avaliação.

A implementação anterior que favorecia maior preço no último critério deve ser corrigida.

A pontuação é uma ferramenta de decisão da V1. Não deve ser tratada como verdade universal sobre valor da oferta.

---

## 15. Taxonomia V1 — estrutura de trabalho

### Casa & Jardim

- Decoração
- Cozinha & Mesa
- Organização
- Limpeza & Cuidados da Casa
- Ferramentas & Manutenção
- Jardim
- Móveis
- Festa & Eventos

### Beleza & Cuidados

- Cabelos
- Maquiagem
- Unhas & Manicure
- Pele & Rosto
- Corpo & Higiene
- Perfumes & Fragrâncias
- Cílios & Sobrancelhas
- Ferramentas & Acessórios de Beleza

### Moda

- Roupas
- Calçados

Características como público, estilo e tipo devem preferencialmente ser atributos, e não novas categorias públicas.

### Moda & Acessórios

- Joias & Bijuterias
- Acessórios para Cabelo
- Óculos
- Bolsas & Carteiras
- Bonés & Chapéus
- Relógios

`Outros Acessórios` não deve ser categoria pública.

### Infantil

- Bebê
- Roupas
- Calçados
- Acessórios

### Tecnologia & Eletrônicos

- Celulares & Acessórios
- Computadores & Periféricos
- Componentes & Peças
- Redes & Conectividade
- Impressão & Digitalização
- Áudio
- Games & Consoles
- Smartwatches & Wearables
- Foto, Vídeo & Conteúdo

### Veículos

- Peças para Carros
- Peças para Motos
- Acessórios para Carros
- Acessórios para Motos
- Cuidados Automotivos
- Ferramentas & Diagnóstico

### Papelaria & Artesanato

- Cadernos & Papel
- Escrita & Correção
- Organização Escolar & Escritório
- Arte & Artesanato
- Presentes & Embalagens

### Esportes & Lazer

- Roupas Esportivas
- Calçados Esportivos
- Equipamentos Esportivos
- Acessórios Esportivos

### Pets

- Alimentação
- Higiene & Banho
- Brinquedos & Entretenimento
- Acessórios
- Roupas
- Cuidados de Saúde

### Alimentos & Bebidas

- Alimentos
- Bebidas
- Ingredientes & Temperos
- Doces & Snacks

### Saúde & Bem-estar

- Suplementos
- Cuidados & Bem-estar
- Equipamentos & Produtos de Saúde

A taxonomia está funcionalmente consolidada, mas a política de elegibilidade para Saúde ainda precisa de aprovação explícita.

### Brinquedos & Jogos

Área própria para brinquedos e jogos identificados como tais, independentemente da categoria original do parceiro.

### Presentes & Personalizados

Área transversal. Deve receber produtos cuja natureza comercial seja efetivamente presente/personalização, e não qualquer produto que apenas possa ser oferecido como presente.

### Livros & Conhecimento

Área própria para livros e conteúdos equivalentes.

### Viagem & Bagagem

Área própria para produtos de viagem e bagagem.

---

## 16. Atributos versus categorias

Não criar categorias para cada característica.

Candidatos naturais a atributos:

- masculino;
- feminino;
- unissex;
- plus size;
- fitness;
- casual;
- profissional;
- kit;
- tipo específico de produto;
- animal do produto;
- outras características que cruzem várias categorias.

O objetivo é evitar explosão da árvore de categorias.

---

## 17. Regras de classificação

O normalizador deve usar sinais combinados:

```text
categoria do parceiro
+
subcategoria do parceiro
+
título
+
atributos disponíveis
```

A regra de classificação deve privilegiar a natureza real do produto.

### Exemplos comprovados durante a análise

- produtos em `Mom & Baby` podem ser brinquedos, enxoval, higiene, alimentação etc.;
- `Beauty Sets & Packages` mistura kits de maquiagem, skincare, higiene e outros formatos;
- `Mobile & Gadgets / Others` mostrou várias peças de reposição de celular;
- `Home Appliances` mistura aparelhos, peças e componentes elétricos;
- `Hobbies & Collections` mistura jogos, colecionáveis, instrumentos, artesanato e souvenirs;
- categorias como `Decoration` e `Home Organizers` contêm itens que precisam ser redistribuídos.

A conclusão geral é que a taxonomia do parceiro é uma pista, não uma autoridade final.

---

## 18. Elegibilidade — regras já identificadas

### 18.1 Bebidas alcoólicas

**Não elegíveis para a vitrine.**

### 18.2 Produtos sem imagem válida

**Não entram na vitrine.**

### 18.3 Produtos sem link válido

**Não entram na vitrine.**

### 18.4 Produtos sem avaliação válida quando a regra da seleção exigir avaliação

Não devem entrar na seleção normal de melhores ofertas.

### 18.5 Produtos sem classificação confiável

Não forçar classificação. Permanecem fora da vitrine até que exista regra confiável.

### 18.6 Validade

Oferta expirada não deve permanecer ativa.

### 18.7 Saúde e saúde veterinária

Ainda requerem política específica de elegibilidade antes de automação definitiva.

---

## 19. Drogasmil — escopo já aprovado

Podem ser considerados produtos da Drogasmil, sujeito às regras gerais:

- higiene;
- cosméticos;
- beleza;
- cuidados pessoais não farmacêuticos;
- itens para casa/conveniência;
- outros produtos não farmacêuticos.

Medicamentos não devem ser tratados como automaticamente elegíveis.

---

## 20. Shopee — normalização

Regras já definidas:

- `itemid` → `id`, no formato `shopee-{itemid}`;
- toda oferta Shopee → `loja = "Shopee"`;
- `title` → `nome`, com trim apenas;
- categoria → taxonomia Mário Holanda;
- imagem e link devem vir da fonte, sem substituição improvisada;
- `product_short link` e demais campos brutos são dados de origem, não modelo público final.

A taxonomia final deve ser baseada também no conteúdo, não somente em `global_category1`/`global_category2`.

---

## 21. Arquitetura lógica recomendada

```text
                ┌────────────────────┐
                │     Parceiros      │
                │ Shopee/Amazon/etc. │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │     Aquisição      │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Validação Estrut.  │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │    Normalização    │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │    Elegibilidade   │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │      Ranking       │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Seleção/Distrib.   │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Estado + Histórico │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Validação Final    │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │   ofertas.json     │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │    Publicação      │
                └────────────────────┘
```

O motor deve evitar acoplamento entre aquisição de um parceiro e as regras gerais de seleção.

---

## 22. Contrato de modularidade para futuros afiliados

O projeto deve separar claramente:

### Núcleo reutilizável

- modelo de oferta;
- validação;
- normalização;
- elegibilidade;
- ranking;
- distribuição;
- estado;
- histórico;
- publicação;
- observabilidade;
- testes.

### Camada de parceiro

- como baixar o feed;
- como mapear campos da fonte;
- como preservar tracking;
- quais particularidades de dados existem.

### Camada de marca/afiliado

- identidade visual;
- nome da marca;
- categorias expostas publicamente;
- regras comerciais específicas;
- comissões e configurações específicas.

O objetivo é permitir que um novo afiliado utilize o mesmo motor com configuração e adaptadores diferentes.

---

## 23. Preparação para escala

A evolução futura poderá incluir:

- novos parceiros;
- novos tipos de feed;
- diferentes limites de seleção;
- diferentes regras de elegibilidade por afiliado;
- diferentes taxonomias públicas com um mesmo núcleo de dados;
- painéis e relatórios;
- aprendizagem baseada em dados históricos;
- novas estratégias de ranking.

Essas possibilidades não fazem parte da V1 obrigatória, mas a arquitetura deve evitar bloqueá-las.

---

## 24. Backlog atual

### PENDÊNCIA 001 — Validação de feed/source

Subtarefas esperadas:

- validar arquivo recebido;
- validar cabeçalhos;
- validar colunas obrigatórias;
- detectar arquivo vazio/truncado;
- produzir erro explícito;
- não publicar em caso de falha crítica.

### PENDÊNCIA 002 — Atualização segura/atômica de `ofertas.json`

Subtarefas esperadas:

- construir novo conteúdo em arquivo temporário;
- validar JSON;
- validar estrutura;
- substituir apenas após sucesso completo;
- manter última versão válida caso algo falhe.

### PENDÊNCIA 003 — Eliminar caminhos fixos/absolutos na automação

Subtarefas esperadas:

- resolver caminhos relativos ao projeto;
- evitar dependência do diretório pessoal atual;
- parametrizar entradas/saídas;
- manter execução local e automatizada consistente.

Novas necessidades devem preferencialmente ser adicionadas como subtarefas das pendências existentes, evitando proliferação desnecessária de códigos de pendência.

---

## 25. Critérios de pronto da V1

A automação somente deve ser considerada pronta quando:

- o feed é adquirido com segurança;
- a estrutura é validada;
- produtos são normalizados para o modelo permanente;
- elegibilidade é aplicada antes do ranking;
- duplicações são controladas por ID estável;
- ranking usa o desempate correto;
- distribuição por loja respeita os limites;
- validade é aplicada;
- falhas críticas não sobrescrevem a última publicação válida;
- `ofertas.json` é gerado de forma atômica;
- execução gera relatório;
- testes cobrem os principais casos positivos e negativos;
- documentação e código estão alinhados.

---

## 26. Regra de evolução pós-V1

A taxonomia, o ranking e a elegibilidade devem ser considerados **configuráveis e revisáveis**, não dogmas.

Mudanças futuras devem seguir:

```text
observação real
   ↓
análise
   ↓
decisão registrada
   ↓
teste
   ↓
implementação
   ↓
validação
   ↓
publicação
```

Nenhuma IA futura deve modificar regras estruturais apenas por “achar melhor”. Mudanças relevantes devem ser justificadas e registradas.

---

## 27. Uso por IAs codadoras

Qualquer IA codadora deve, antes de alterar o sistema:

1. ler o Documento Mestre;
2. ler o documento da etapa específica;
3. identificar o requisito aplicável;
4. evitar criar regras conflitantes;
5. propor mudanças quando houver ambiguidade;
6. atualizar a documentação quando uma mudança aprovada alterar o comportamento do sistema.

### Regra de segurança para IA

> **Não inventar dados, regras, campos ou comportamentos que não estejam definidos ou aprovados.**

Quando faltar especificação, a IA deve sinalizar a lacuna em vez de preencher com suposição silenciosa.

---

## 28. Estado do documento

Esta é uma consolidação de alto nível para orientar a próxima fase.

**Não considerar como aprovação automática de toda regra pendente.**

Itens explicitamente pendentes permanecem pendentes até decisão registrada.
