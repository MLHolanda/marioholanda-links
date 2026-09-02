# 05 — ARQUITETURA DA AUTOMAÇÃO

## 1. Objetivo

A automação do projeto Mário Holanda Ofertas tem como objetivo reduzir o trabalho manual de atualização das ofertas, mantendo segurança, controle, rastreabilidade e possibilidade de recuperação em caso de falha.

A automação deverá evoluir gradualmente.

Princípio fundamental:

> Automatizar somente aquilo que estiver compreendido, definido, validado e testado.

---

## 2. Princípios fundamentais

O sistema deverá seguir estes princípios:

1. Segurança antes de velocidade.
2. Uma mudança por vez.
3. Testar antes de avançar.
4. Nenhuma falha poderá destruir o estado anterior.
5. Dados e lógica devem permanecer separados.
6. IDs devem ser estáveis e únicos.
7. Não criar duplicatas.
8. Não apagar dados sem uma decisão explícita.
9. Git continua sendo ponto de controle.
10. Publicação só acontece após validação.
11. Falhas devem interromper o processo.
12. Processos automáticos devem possuir critérios de segurança.
13. Decisões importantes devem ser documentadas.
14. A complexidade deve ser adicionada somente quando necessária.
15. O sistema deve permitir evolução futura sem comprometer o funcionamento atual.

---

## 3. Fluxo geral

O fluxo previsto para a automação é:

```text
Fonte de ofertas
       ↓
Download
       ↓
Validação do feed
       ↓
Filtragem
       ↓
Regras editoriais
       ↓
Ranking
       ↓
Seleção
       ↓
Conversão para JSON
       ↓
Integração com ofertas.json
       ↓
Validação final
       ↓
Git
       ↓
Publicação
       ↓
Site
---

## 5. Download do feed

O componente:

automacao/baixar_feed.py

é responsável por:

1. Ler o arquivo .env.
2. Obter a URL do feed.
3. Realizar o download.
4. Salvar o feed.
5. Informar o resultado.
6. Interromper o processo em caso de erro.

Um download bem-sucedido não significa automaticamente que o feed é válido.

---

## 6. Filtragem inicial

O componente:

automacao/filtrar_ofertas_v2.py

realiza a filtragem inicial.

As condições atuais incluem:

- desconto mínimo;
- faixa de preço;
- avaliação mínima;
- imagem existente;
- link existente.

A filtragem reduz o universo de produtos antes do ranking.

---

## 7. Regras editoriais

O componente:

automacao/regras_ofertas.py

contém regras para impedir automaticamente produtos considerados inadequados para a vitrine.

A função principal é:

produto_permitido(produto)

As regras editoriais devem permanecer separadas da lógica de ranking.
---

## 8. Ranking

O componente:

automacao/ranking_ofertas_v6.py

calcula uma pontuação para cada produto elegível.

A pontuação considera:

- desconto;
- avaliação;
- preço.

A pontuação máxima é de 100 pontos.

O ranking também utiliza diversidade por categoria.

Configuração atual:

- máximo de ofertas: 50;
- máximo por categoria: 5.

O objetivo é evitar que uma única categoria domine toda a vitrine.

---

## 9. Identidade das ofertas

Toda oferta deve possuir um identificador único e estável.

Ofertas Shopee poderão utilizar:

shopee-ITEMID

Ofertas cadastradas manualmente utilizarão um UUID gerado automaticamente.

O ID não deverá depender da posição da oferta na lista.

---

## 10. Estrutura das ofertas

A estrutura atual de uma oferta é:

id
nome
loja
categoria
preco
precoAntigo
comissao
imagem
link
ativo
---

## 11. Cadastro de ofertas

Somente o administrador do projeto poderá cadastrar ofertas.

Neste estágio, o cadastro será realizado pelo terminal através de Python.

Futuramente poderá existir um painel administrativo protegido.

---

## 12. Campos do cadastro

### Obrigatórios

nome
loja
categoria
preco
imagem
link

### Opcionais

precoAntigo
comissao

### Automáticos

id
ativo

Toda nova oferta será criada como ativa.

---

## 13. Validação do cadastro

Antes da gravação, o sistema deverá validar:

- nome;
- loja;
- categoria;
- preço;
- preço antigo, quando informado;
- comissão, quando informada;
- imagem;
- link;
- coerência dos dados.

O preço atual deverá ser numérico.

O preço antigo, quando informado, deverá ser numérico e maior que o preço atual.

O link deverá possuir formato válido.

Qualquer erro deverá impedir a gravação.
---

## 14. Prévia e confirmação

Antes da gravação definitiva, o sistema deverá apresentar uma prévia completa da oferta.

A gravação somente ocorrerá após confirmação explícita do administrador.

Se o administrador cancelar, nenhum dado deverá ser alterado.

---

## 15. Imagens

O cadastro poderá utilizar:

- URL externa;
- caminho local.

O sistema não fará download automático das imagens nesta fase.

---

## 16. Links

O sistema receberá o link já pronto.

O link deverá ser validado e armazenado sem alteração.

O sistema não deverá fabricar ou modificar links de afiliados automaticamente.

Integrações específicas com cada plataforma poderão ser desenvolvidas futuramente.

---

## 17. Gravação segura

O arquivo oficial das ofertas é:

ofertas.json

O sistema não deverá sobrescrever esse arquivo sem proteção.

O processo deverá seguir:

ofertas.json atual
       ↓
backup
       ↓
validação
       ↓
gravação
       ↓
validação do JSON
       ↓
resultado aprovado

Se ocorrer qualquer erro, o estado anterior deverá ser preservado.
---

## 18. Duplicidades

O sistema não deverá criar ofertas duplicadas.

O ID será utilizado como identidade principal.

Quando uma oferta já existir:

ID encontrado
      ↓
atualizar dados

Quando não existir:

ID não encontrado
      ↓
criar oferta

Conflitos de ID entre origens diferentes deverão interromper o processo para análise.

---

## 19. Ofertas Shopee ausentes

Quando uma oferta Shopee deixar de aparecer em uma atualização considerada válida:

oferta existente
      ↓
não encontrada no novo feed
      ↓
ativo = false

A oferta não deverá ser apagada.

Se ela retornar em uma atualização posterior:

oferta encontrada novamente
      ↓
ativo = true

---

## 20. Proteção contra feed inválido

Um feed vazio, truncado, incompleto ou estruturalmente inválido não poderá provocar desativação em massa.

Antes de qualquer alteração significativa, deverão ser verificadas condições mínimas de integridade do feed.

Os critérios quantitativos serão definidos após análise dos dados reais e do comportamento do fornecedor.
---

## 21. Falhas durante a automação

A regra principal é:

> Falhou → não publica.

Se uma etapa crítica falhar, as etapas seguintes não deverão ser executadas.

O estado anterior deverá permanecer preservado.

---

## 22. Atomicidade da atualização

A atualização deverá seguir este princípio:

processamento
      ↓
resultado válido?
   /          \
 NÃO          SIM
 ↓             ↓
PARAR       CONTINUAR

Não deverá existir publicação parcial.

O objetivo é:

> Ou a atualização inteira é válida, ou o estado anterior permanece.

---

## 23. Orquestração

O componente:

automacao/atualizar_ofertas.py

coordena as etapas da automação.

Fluxo atual:

baixar_feed.py
       ↓
filtrar_ofertas_v2.py
       ↓
ranking_ofertas_v6.py
       ↓
gerar_ofertas_json.py
       ↓
integrar_shopee.py

Se uma etapa retornar erro, o processo deverá ser interrompido.
---

## 24. Fonte oficial do site

O arquivo:

ofertas.json

continua sendo a fonte oficial dos dados utilizados pelo site.

O site carrega esse arquivo através de:

fetch("ofertas.json")

e utiliza os dados para apresentar as ofertas.

---

## 25. Git

Git será utilizado para versionar alterações importantes.

Fluxo recomendado:

alteração
   ↓
teste
   ↓
verificação
   ↓
git status
   ↓
git add
   ↓
git commit
   ↓
git push

O cadastro não deverá executar automaticamente:

git commit
git push

A decisão de publicar permanece sob controle do administrador.

---

## 26. Publicação

A publicação do site ocorre através da Vercel.

Fluxo geral:

GitHub
   ↓
Vercel
   ↓
produção

A automação não deverá publicar alterações sem que o resultado tenha sido validado.
---

## 27. Histórico

O sistema atual armazenará somente o estado atual das ofertas.

O histórico de:

- preços;
- alterações;
- aparecimento;
- desaparecimento;
- desempenho;

será implementado futuramente, preferencialmente em estrutura separada.

---

## 28. Evolução futura

A arquitetura poderá evoluir para:

Cadastro
     ↓
API
     ↓
Banco de dados
     ↓
Painel administrativo
     ↓
Site

Também poderão ser desenvolvidos futuramente:

- monitoramento;
- métricas;
- histórico;
- integração com outras lojas;
- publicação automatizada;
- inteligência para seleção de ofertas;
- auxílio da Athena na análise.

Essas funcionalidades não fazem parte da implementação atual.

---

## 29. Responsabilidade do administrador

O administrador continua sendo responsável pelas decisões de publicação.

A automação deverá:

- processar;
- validar;
- organizar;
- preparar;
- informar resultados;
- interromper diante de falhas.

A automação não deverá tomar decisões críticas que não tenham sido previamente definidas.
---

## 30. Regra máxima do projeto

Nenhuma automação deverá comprometer uma versão funcional existente.

Antes de aumentar o grau de automação:

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
PUBLICAR

Essa sequência deverá ser preservada durante a evolução do projeto.

---

## 31. Decisões aprovadas

Até o momento foram aprovadas as seguintes decisões:

1. Somente o administrador cadastra ofertas.
2. Campos obrigatórios e opcionais foram definidos.
3. Links são recebidos, validados e não modificados.
4. Imagens podem ser externas ou locais.
5. IDs são gerados automaticamente quando necessário.
6. Ofertas podem ser desativadas sem serem apagadas.
7. O cadastro inicial será feito pelo terminal.
8. A gravação será protegida por backup e validação.
9. Os campos serão rigorosamente validados.
10. O cadastro terá prévia e confirmação.
11. O cadastro não publicará automaticamente.
12. Não serão criadas duplicatas.
13. O histórico será implementado futuramente.
14. Ofertas Shopee ausentes serão desativadas somente após atualização válida.
15. Falhas críticas preservarão o estado anterior.

---

## 32. Estado desta documentação

Este documento representa as decisões arquiteturais aprovadas até esta etapa.

Nenhuma implementação futura deverá contrariar estas decisões sem que a decisão seja revisada e documentada novamente.

