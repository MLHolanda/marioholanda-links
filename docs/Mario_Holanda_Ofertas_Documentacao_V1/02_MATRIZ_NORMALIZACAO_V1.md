# Mário Holanda Ofertas — Matriz de Normalização V1

## 1. Regra central

```text
Fonte do parceiro
      ↓
Categoria original
+
Subcategoria original
+
Título
+
Atributos
      ↓
Classificação Mário Holanda
```

Nunca tratar a categoria do parceiro como verdade absoluta.

## 2. Mapeamentos confirmados

| Origem | Destino |
|---|---|
| Home & Living / Decoration | Casa & Jardim → Decoração |
| Home & Living / Kitchenware | Casa & Jardim → Cozinha & Mesa |
| Home & Living / Dinnerware | Casa & Jardim → Cozinha & Mesa |
| Home & Living / Home Organizers | Casa & Jardim → Organização |
| Home & Living / Home Care Supplies | Casa & Jardim → Limpeza & Cuidados da Casa, com redistribuição quando necessário |
| Home & Living / Tools & Home Improvement | Casa & Jardim → Ferramentas & Manutenção, com redistribuição quando necessário |
| Home & Living / Gardening | Casa & Jardim → Jardim |
| Home & Living / Furniture | Casa & Jardim → Móveis, com redistribuição de peças/acessórios |
| Home & Living / Party Supplies | Casa & Jardim → Festa & Eventos, com redistribuição quando necessário |
| Beauty / Hair Care | Beleza & Cuidados → Cabelos |
| Beauty / Makeup | Beleza & Cuidados → Maquiagem |
| Beauty / Hand, Foot & Nail Care | Beleza & Cuidados → Unhas & Manicure |
| Beauty / Skincare | Beleza & Cuidados → Pele & Rosto |
| Beauty / Bath & Body Care | Beleza & Cuidados → Corpo & Higiene |
| Beauty / Perfumes & Fragrances | Beleza & Cuidados → Perfumes & Fragrâncias |
| Beauty / Beauty Tools | Beleza & Cuidados → Ferramentas & Acessórios de Beleza |
| Beauty / Beauty Sets & Packages | Redistribuir pelo conteúdo |
| Beauty / Others | Não forçar |
| Women Clothes | Moda → Roupas |
| Men Clothes | Moda → Roupas |
| Women Shoes | Moda → Calçados |
| Men Shoes | Moda → Calçados |
| Fashion Accessories | Moda & Acessórios, conforme natureza |
| Baby & Kids Fashion | Infantil, conforme natureza |
| Mom & Baby | Redistribuir conforme natureza |
| Mobile & Gadgets | Tecnologia & Eletrônicos, conforme natureza |
| Computers & Accessories | Tecnologia & Eletrônicos, conforme natureza |
| Spare Parts and Accessories for Vehicles | Veículos, conforme natureza |
| Sports & Outdoors | Esportes & Lazer, conforme natureza |
| Health | Saúde & Bem-estar, sujeito à elegibilidade |
| Pets | Pets, sujeito à elegibilidade |
| Food & Beverages | Alimentos & Bebidas, sujeito às regras de validade/elegibilidade |
| Hobbies & Collections | Redistribuir conforme natureza |
| Home Appliances | Casa & Jardim / Tecnologia, conforme natureza do item |
| Automobiles | Veículos |
| Motorcycles | Veículos |
| Cameras & Drones | Tecnologia & Eletrônicos → Foto, Vídeo & Conteúdo |
| Gaming & Consoles | Tecnologia & Eletrônicos → Games & Consoles |
| Watches | Moda & Acessórios → Relógios |
| Women Bags | Moda & Acessórios → Bolsas & Carteiras |
| Men Bags | Moda & Acessórios → Bolsas & Carteiras |
| Books & Magazines | Livros & Conhecimento |
| Travel & Luggage | Viagem & Bagagem |
| Audio | Tecnologia & Eletrônicos → Áudio |

## 3. Casos que exigem leitura do produto

### Kits

Não são categoria. A categoria é determinada pelo conteúdo.

### `Others`

Não é destino automático. Se não for possível classificar com confiança, não publicar.

### Categorias muito amplas

Exemplos: `Mom & Baby`, `Hobbies & Collections`, `Home Appliances`.

Essas categorias devem ser tratadas como origem e redistribuídas quando necessário.

### Produtos deslocados

Casos observados incluem:

- acetona dentro de `Printers & Scanners`;
- fonte para parafusadeira dentro de `Network Components`;
- pote de cozinha dentro de `Vehicular Tools`;
- material de costura em categoria de eletrodoméstico;
- peças automotivas ou de celular em grupos genéricos.

Esses casos justificam a regra de normalização por natureza real.

## 4. Saída da normalização

O resultado da normalização deve conter, no mínimo:

- categoria interna;
- sinais usados para a decisão, quando necessário para diagnóstico;
- status de confiança/regra, se previsto na implementação;
- vínculo com o ID original.

A implementação não deve expor internamente ao usuário final toda a lógica de decisão.
