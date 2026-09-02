# Mário Holanda Ofertas — Contrato para IA Codadora V1

## 1. Objetivo

Este documento orienta qualquer IA utilizada para implementar, revisar, testar ou modificar o projeto.

A IA deve tratar os documentos do projeto como fonte de verdade.

## 2. Antes de alterar código

A IA deve:

1. ler a documentação relevante;
2. verificar o estado atual do código;
3. identificar arquivos afetados;
4. verificar se há regra já aprovada para o comportamento;
5. propor mudança quando houver conflito ou lacuna.

## 3. Não inventar

A IA não deve inventar silenciosamente:

- dados de produto;
- preços antigos;
- avaliações;
- descontos;
- validade;
- categorias;
- comissões;
- regras comerciais;
- campos permanentes.

## 4. Não espalhar regras

Regras de negócio devem ficar centralizadas e configuráveis sempre que tecnicamente adequado.

Evitar lógica duplicada do tipo:

```python
if category == "...":
    ...
```

em dezenas de arquivos.

## 5. Separação obrigatória

Preservar separação entre:

```text
Fonte
Normalização
Elegibilidade
Ranking
Estado
Publicação
```

Uma mudança de parceiro não deve exigir alteração manual da lógica central quando o comportamento for genericamente reutilizável.

## 6. Segurança

Não versionar:

- tokens;
- secrets;
- URLs privadas de feed;
- credenciais;
- chaves de APIs.

Segredos devem ser carregados por ambiente/configuração segura.

## 7. Falhas críticas

A IA não deve implementar uma rotina que publique `ofertas.json` parcialmente validado.

A atualização pública deve ser atômica.

## 8. Testes mínimos

Toda mudança de regra deve ter teste ou validação equivalente para:

- caso válido;
- caso inválido;
- caso limítrofe;
- regressão da regra anterior.

## 9. Documentação sincronizada

Quando uma mudança aprovada altera comportamento do sistema:

```text
código
+
teste
+
documentação
```

devem evoluir juntos.

## 10. Resultado esperado da IA

Ao concluir uma tarefa, a IA deve informar:

- o que mudou;
- quais arquivos foram afetados;
- quais regras foram aplicadas;
- quais testes foram executados;
- quais limitações ou pendências permanecem.

## 11. Regra de ouro

> **Uma IA codadora implementa a decisão do projeto; ela não substitui a decisão do projeto.**
