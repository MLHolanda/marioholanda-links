# 04 — ARQUITETURA DE OFERTAS

## 1. Objetivo

O sistema de ofertas do projeto Mário Holanda Ofertas tem como objetivo permitir o cadastro, organização, exibição e futura automação de ofertas e links de afiliados.

A evolução do sistema deverá seguir uma construção gradual, segura e testável.

Fluxo principal:

```text
Encontrar uma oferta
        ↓
Cadastrar a oferta
        ↓
Validar os dados
        ↓
Guardar os dados
        ↓
Exibir no site
        ↓
Futuramente automatizar
```

---

## 2. Fonte oficial dos dados

O arquivo `ofertas.json` é a fonte oficial dos dados das ofertas.

O `script.js` é responsável por carregar esses dados através de `fetch()` e utilizá-los para exibir as ofertas no site.

Arquitetura atual:

```text
ofertas.json
      ↓
   fetch()
      ↓
  script.js
      ↓
     site
```

Os dados das ofertas não devem ser mantidos diretamente dentro do código de funcionamento do site.

---

## 3. Estrutura de uma oferta

Cada oferta possui atualmente os seguintes campos:

```text
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
```

### Descrição dos campos

* `id` — identificador único da oferta.
* `nome` — nome ou descrição principal do produto/oferta.
* `loja` — loja ou plataforma onde a oferta está disponível.
* `categoria` — categoria da oferta.
* `preco` — preço atual, quando disponível.
* `precoAntigo` — preço anterior, quando disponível.
* `comissao` — comissão prevista, quando conhecida.
* `imagem` — caminho da imagem utilizada no site.
* `link` — link da oferta, preferencialmente o link de afiliado.
* `ativo` — indica se a oferta pode ser utilizada pelo sistema.

---

## 4. Separação entre dados e lógica

Uma regra fundamental da arquitetura é manter os dados separados da lógica do sistema.

### Dados

Os dados das ofertas ficam em:

```text
ofertas.json
```

### Lógica

O comportamento do site fica em:

```text
script.js
```

### Estrutura visual

A estrutura da página fica em:

```text
index.html
```

### Aparência

A aparência visual fica em:

```text
style.css
```

Essa separação facilita a manutenção e permite evoluir o sistema sem precisar alterar o código principal sempre que uma nova oferta for cadastrada.

---

## 5. Estrutura atual do projeto

A estrutura relevante atualmente é:

```text
marioholanda-links/
│
├── index.html
├── style.css
├── script.js
├── ofertas.json
├── ofertas.js
│
├── img/
│
├── .gitignore
├── CNAME
└── .vercel/
```

O arquivo `ofertas.js` não faz mais parte do funcionamento atual do site.

Ele foi mantido temporariamente no projeto como histórico/referência e poderá ser removido futuramente, após nova verificação.

---

## 6. Cadastro futuro de ofertas

A próxima evolução planejada é criar uma forma mais simples de cadastrar ofertas.

O objetivo é evitar que seja necessário editar manualmente o arquivo `ofertas.json` para cada nova oferta.

Fluxo planejado:

```text
             NOVA OFERTA
                  ↓
        Cadastro dos dados
                  ↓
              Validação
                  ↓
           ofertas.json
                  ↓
                site
```

O cadastro deverá futuramente validar, entre outros pontos:

* nome obrigatório;
* loja obrigatória;
* link obrigatório;
* imagem válida;
* preço numérico quando informado;
* identificador único;
* situação da oferta (`ativo`).

---

## 7. Automação futura

A automação será desenvolvida gradualmente.

### Fase 1 — Cadastro

Facilitar o cadastro de novas ofertas.

### Fase 2 — Links

Auxiliar no processo de utilização dos links de afiliados.

### Fase 3 — Publicação

Automatizar, quando tecnicamente e comercialmente permitido, a publicação das ofertas nos canais definidos pelo projeto.

### Fase 4 — Monitoramento

Registrar e acompanhar informações como:

* cliques;
* desempenho;
* ofertas ativas;
* ofertas expiradas;
* desempenho por loja;
* desempenho por categoria.

### Fase 5 — Inteligência

Utilizar dados acumulados para auxiliar na tomada de decisões e na identificação de ofertas com melhor desempenho.

---

## 8. Princípios da arquitetura

O desenvolvimento deverá seguir estes princípios:

1. Uma mudança por vez.
2. Testar antes de avançar.
3. Versionar alterações importantes com Git.
4. Não remover componentes sem antes verificar suas dependências.
5. Separar dados, lógica e apresentação.
6. Priorizar soluções simples antes de soluções complexas.
7. Não automatizar processos que ainda não estejam bem compreendidos.
8. Validar as regras específicas de cada programa de afiliados antes de automatizar seus links ou processos.
9. Manter a possibilidade de voltar a um estado anterior através do Git.
10. Documentar decisões importantes da arquitetura.

---

## 9. Estado atual

A primeira etapa da arquitetura foi concluída.

O site passou a utilizar:

```text
ofertas.json
      ↓
    fetch()
      ↓
  script.js
      ↓
     site
```

O carregamento do JSON foi testado localmente e confirmado através do navegador.

O antigo carregamento de `ofertas.js` foi removido do `index.html`.

A alteração foi registrada no Git.

### Commits relacionados

```text
81e9ab5
feat: adiciona estrutura inicial de ofertas

834b4d4
feat: carrega ofertas pelo arquivo JSON

9960da5
refactor: remove dependencia do ofertas.js
```

---


## 10. Próximo passo

O próximo passo do projeto será analisar e definir o funcionamento do cadastro simplificado de ofertas.

Antes da implementação, deverão ser definidos:

* quem poderá cadastrar;
* quais campos serão obrigatórios;
* como o link será tratado;
* como as imagens serão armazenadas;
* como o `id` será gerado;
* como uma oferta será ativada ou desativada;
* onde o cadastro será executado;
* como os dados serão gravados;
* como o sistema será validado.

Nenhuma dessas decisões deverá ser implementada antes de sua definição e validação.
