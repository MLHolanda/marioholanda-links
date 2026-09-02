# Mário Holanda Ofertas — Taxonomia V1

## 1. Objetivo

Definir a linguagem interna utilizada pelo Mário Holanda Ofertas para classificar produtos, independentemente da taxonomia do parceiro.

## 2. Princípios

- A taxonomia do parceiro é apenas sinal.
- A natureza real do produto é prioritária.
- Não forçar classificação.
- Não criar categoria para cada atributo.
- Manter a árvore enxuta.
- Permitir evolução futura sem quebrar IDs.

## 3. Áreas principais V1

```text
Casa & Jardim
Beleza & Cuidados
Moda
Moda & Acessórios
Infantil
Tecnologia & Eletrônicos
Veículos
Papelaria & Artesanato
Esportes & Lazer
Pets
Alimentos & Bebidas
Saúde & Bem-estar
Brinquedos & Jogos
Presentes & Personalizados
Livros & Conhecimento
Viagem & Bagagem
```

## 4. Árvore V1

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

### Moda & Acessórios
- Joias & Bijuterias
- Acessórios para Cabelo
- Óculos
- Bolsas & Carteiras
- Bonés & Chapéus
- Relógios

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

### Brinquedos & Jogos
- Área própria; aprofundamento interno opcional em versões futuras.

### Presentes & Personalizados
- Área transversal.

### Livros & Conhecimento
- Área própria.

### Viagem & Bagagem
- Área própria.

## 5. Atributos que não devem virar categorias automaticamente

- masculino;
- feminino;
- unissex;
- plus size;
- fitness;
- casual;
- profissional;
- kit;
- tipo de produto;
- animal;
- temática.

## 6. Conceitos deliberadamente não adotados

### `Mom & Baby`
Não é categoria principal. Seus produtos são redistribuídos conforme a natureza real.

### `Hobbies & Collections`
Não é categoria principal. Produtos são redistribuídos conforme a natureza real.

### `Others`
Não é categoria de destino. Produto mal classificado não deve ser despejado em “Outros”.

### `Outros Acessórios`
Não deve ser categoria pública.

### `Peças & Reposição` como categoria universal
Não utilizar como categoria pública transversal. A classificação de peça deve permanecer contextualizada pela área do produto.

## 7. IDs estáveis de categoria

A implementação deverá usar identificadores estáveis em vez de depender do texto exibido.

Exemplos sugeridos:

```text
CASA_JARDIM
BELEZA_CUIDADOS
MODA
MODA_ACESSORIOS
INFANTIL
TECNOLOGIA
VEICULOS
PAPELARIA_ARTESANATO
ESPORTES_LAZER
PETS
ALIMENTOS_BEBIDAS
SAUDE_BEM_ESTAR
BRINQUEDOS_JOGOS
PRESENTES_PERSONALIZADOS
LIVROS_CONHECIMENTO
VIAGEM_BAGAGEM
```

A lista acima é um identificador conceitual; a implementação pode escolher outra convenção consistente, desde que estável e documentada.
