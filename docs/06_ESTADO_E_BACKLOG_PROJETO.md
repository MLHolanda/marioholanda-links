# 06 — ESTADO E BACKLOG DO PROJETO

## 1. Objetivo

Este documento é o registro central do estado técnico do projeto Mário Holanda Ofertas.

Seu objetivo é preservar decisões, pendências, problemas identificados, soluções já realizadas e próximos passos.

Ele existe para que o projeto não dependa exclusivamente do histórico das conversas.

---

## 2. Regra de continuidade

Nenhuma pendência técnica identificada durante o desenvolvimento deverá ser esquecida.

Toda pendência deverá permanecer registrada até ser:

- resolvida;
- testada;
- documentada;
- marcada como concluída.

Uma pendência não poderá ser considerada concluída apenas porque o código aparentemente funciona.

---

## 3. Regra de segurança

O projeto deverá preservar uma versão funcional antes de qualquer alteração estrutural importante.

Antes de implementar uma mudança:

ANALISAR
   ↓
DEFINIR
   ↓
DOCUMENTAR
   ↓
REVISAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
VALIDAR
   ↓
PUBLICAR
---

## 4. Estado atual do projeto

O site utiliza atualmente:

ofertas.json
     ↓
fetch()
     ↓
script.js
     ↓
site

O arquivo ofertas.json é a fonte oficial dos dados exibidos pelo site.

A automação Shopee está organizada em:

automacao/
├── atualizar_ofertas.py
├── baixar_feed.py
├── filtrar_ofertas_v2.py
├── ranking_ofertas_v6.py
├── gerar_ofertas_json.py
├── integrar_shopee.py
└── regras_ofertas.py

A configuração do feed está em:

.env

A variável utilizada atualmente é:

SHOPEE_FEED_URL

O arquivo .env não deve ser versionado.

---

## 5. Fluxo atual da automação

O orquestrador executar atualmente as seguintes etapas:

1. baixar_feed.py
2. filtrar_ofertas_v2.py
3. ranking_ofertas_v6.py
4. gerar_ofertas_json.py
5. integrar_shopee.py

Fluxo:

Feed Shopee
    ↓
Download
    ↓
Filtro
    ↓
Regras editoriais
    ↓
Ranking
    ↓
Seleção
    ↓
JSON
    ↓
Integração
    ↓
ofertas.json
    ↓
Site

---

## 6. Estado atual dos dados

O projeto possui atualmente ofertas de diferentes origens.

As ofertas Shopee são identificadas pelo padrão:

shopee-ITEMID

A integração da Shopee substitui somente as ofertas identificadas como Shopee.

Ofertas de outras plataformas permanecem no arquivo.

O arquivo ofertas.json deve continuar sendo preservado como fonte oficial do site.
---

## 7. Pendências técnicas identificadas

### PENDÊNCIA 001 — Validação estrutural do feed

Status: PENDENTE

O download do feed pode ser concluído com sucesso mesmo que o conteúdo esteja vazio, truncado, incompleto ou estruturalmente inválido.

É necessário criar uma etapa independente de validação do feed antes que seus dados possam provocar alterações no catálogo.

A validação deverá impedir que um feed inválido provoque desativação em massa ou atualização incorreta.

Os critérios exatos ainda deverão ser definidos após análise dos dados reais.

---

### PENDÊNCIA 002 — Atualização atômica do ofertas.json

Status: PENDENTE

A integração atual grava diretamente o arquivo ofertas.json.

É necessário evoluir esse processo para uma gravação realmente segura.

Fluxo desejado:

ofertas.json atual
       ↓
backup seguro
       ↓
preparar novo arquivo
       ↓
validar novo arquivo
       ↓
substituição segura
       ↓
validação final

Se qualquer etapa falhar, o arquivo anterior deverá permanecer intacto.

---

## 8. Regra para novas pendências

Toda nova pendência identificada durante análise, implementação ou testes deverá receber:

- número único;
- descrição;
- motivo;
- status;
- etapa prevista para resolução.

Nenhuma pendência deverá ser removida do registro sem que sua resolução tenha sido confirmada por teste.
---

## 9. Decisões aprovadas

### DECISÃO 001 — Controle do cadastro

Somente o administrador poderá cadastrar ofertas.

Status: APROVADA

---

### DECISÃO 002 — Campos da oferta

Campos obrigatórios:

nome
loja
categoria
preco
imagem
link

Campos opcionais:

precoAntigo
comissao

Campos automáticos:

id
ativo

Status: APROVADA

---

### DECISÃO 003 — Tratamento dos links

Os links serão recebidos, validados e armazenados sem alteração.

O sistema não deverá fabricar ou modificar links de afiliados automaticamente.

Status: APROVADA

---

### DECISÃO 004 — Imagens

As imagens poderão utilizar URL externa ou caminho local.

O sistema não fará download automático das imagens nesta fase.

Status: APROVADA

---

### DECISÃO 005 — Identificação

Toda oferta deverá possuir ID único e estável.

Ofertas Shopee utilizarão o padrão:

shopee-ITEMID

Ofertas cadastradas manualmente utilizarão UUID.

Status: APROVADA

---

### DECISÃO 006 — Ativação

Novas ofertas serão criadas como ativas.

Ofertas poderão ser desativadas sem serem apagadas.

Status: APROVADA

---

### DECISÃO 007 — Cadastro inicial

O cadastro inicial será realizado pelo terminal através de Python.

Futuramente poderá existir um painel administrativo protegido.

Status: APROVADA

---

### DECISÃO 008 — Gravação segura

Alterações no ofertas.json deverão possuir proteção por backup e validação.

Status: APROVADA
---

### DECISÃO 009 — Validação

Os dados deverão ser rigorosamente validados antes da gravação.

Qualquer erro deverá impedir a gravação.

Status: APROVADA

---

### DECISÃO 010 — Prévia e confirmação

Antes da gravação definitiva, o sistema deverá apresentar uma prévia completa da oferta.

A gravação somente ocorrerá após confirmação explícita do administrador.

Se houver cancelamento, nenhum dado deverá ser alterado.

Status: APROVADA

---

### DECISÃO 011 — Publicação

O cadastro não deverá publicar automaticamente alterações no site.

A publicação continuará sob controle do administrador.

Status: APROVADA

---

### DECISÃO 012 — Duplicidades

O sistema não deverá criar ofertas duplicadas.

O ID será utilizado como identidade principal.

Conflitos de ID deverão interromper o processo para análise.

Status: APROVADA

---

### DECISÃO 013 — Histórico

O histórico de preços, alterações, aparecimento, desaparecimento e desempenho será implementado futuramente.

Status: APROVADA

---

### DECISÃO 014 — Ofertas Shopee ausentes

Uma oferta Shopee que desaparecer de um feed considerado válido será desativada, e não apagada.

Se retornar posteriormente, poderá ser reativada.

Um feed inválido não poderá provocar desativação em massa.

Status: APROVADA

---

### DECISÃO 015 — Falhas críticas

Se uma etapa crítica da automação falhar, as etapas seguintes não deverão ser executadas.

A atualização deverá ser interrompida.

O estado anterior deverá permanecer preservado.

A regra é:

Falhou → não publica.

Status: APROVADA
---

## 10. Pendências recuperadas de etapas anteriores

As pendências identificadas em conversas e etapas anteriores do projeto deverão ser recuperadas, analisadas e registradas neste documento.

Uma pendência antiga somente será considerada concluída quando houver confirmação de que:

1. foi implementada;
2. foi testada;
3. não criou regressão;
4. a solução foi documentada.

Quando houver dúvida sobre o estado de uma pendência antiga, ela deverá permanecer como:

Status: A VERIFICAR

Não será permitido considerar uma pendência resolvida apenas por suposição.

---

## 11. Separação entre decisões e pendências

Decisões aprovadas representam regras que o projeto deverá seguir.

Pendências representam problemas, riscos ou trabalhos ainda não concluídos.

Uma decisão aprovada não será removida porque existe uma pendência relacionada a ela.

Exemplo:

DECISÃO:
A atualização deve ser segura.

PENDÊNCIA:
Implementar gravação realmente atômica.

A decisão permanece aprovada até que uma nova decisão formal a substitua.

---

## 12. Controle de conclusão

Quando uma pendência for resolvida, seu registro deverá permanecer no histórico.

Exemplo:

PENDÊNCIA 001
Status: CONCLUÍDA

Solução:
Descrição da solução implementada.

Teste:
Descrição do teste realizado.

Data:
Data da conclusão.

Dessa forma, o projeto manterá o histórico do que foi identificado e de como foi resolvido.
---

## 13. Controle de continuidade do projeto

Este documento deverá ser consultado antes de iniciar uma nova etapa técnica importante.

Antes de implementar qualquer alteração, verificar:

- decisões aprovadas;
- pendências abertas;
- pendências em análise;
- testes ainda necessários;
- riscos conhecidos;
- dependências existentes.

Nenhuma nova implementação deverá ignorar uma pendência crítica já registrada.

---

## 14. Regra de não regressão

Uma alteração nova não poderá ser considerada concluída somente porque a nova funcionalidade funciona.

Também deverá ser verificado se:

- o site continua funcionando;
- as ofertas existentes continuam preservadas;
- as ofertas de outras plataformas continuam funcionando;
- os links continuam corretos;
- a automação anterior continua funcionando;
- nenhuma decisão aprovada foi violada.

---

## 15. Próximo passo

Antes da implementação de novas funcionalidades:

1. concluir a revisão crítica da arquitetura;
2. recuperar e registrar as pendências anteriores;
3. definir a prioridade das pendências;
4. definir os testes necessários;
5. somente então iniciar a implementação.

---

## 16. Regra de encerramento

Uma etapa somente será considerada concluída quando houver:

- implementação;
- teste;
- validação;
- documentação;
- registro no Git, quando aplicável.

O projeto deverá sempre manter registrado o ponto exato em que o trabalho foi interrompido.

---

## 17. Estado deste documento

Este documento está em construção.

As informações serão atualizadas conforme novas decisões, pendências, testes e soluções forem identificados.

Nenhuma informação deverá ser apagada simplesmente por ter sido substituída.

Quando uma decisão ou pendência mudar de estado, o histórico deverá permanecer registrado.

