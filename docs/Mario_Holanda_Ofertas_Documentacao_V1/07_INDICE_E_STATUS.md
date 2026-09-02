# Índice da Documentação — Mário Holanda Ofertas V1

| Arquivo | Finalidade | Status |
|---|---|---|
| `00_DOCUMENTO_MESTRE.md` | Fonte de verdade geral do projeto | Base V1 |
| `01_TAXONOMIA_V1.md` | Estrutura de categorias internas | Consolidada para revisão/aprovação |
| `02_MATRIZ_NORMALIZACAO_V1.md` | Regras de tradução da fonte para a taxonomia | Consolidada para implementação posterior |
| `03_REGRAS_ELEGIBILIDADE_V1.md` | Critérios de entrada na vitrine | V1 aprovada; política conservadora para Saúde/Pets |
| `04_CONTRATO_IA_CODADORA.md` | Regras para IAs que implementam/revisam o sistema | Base V1 |
| `05_ESTRATEGIA_AFLIADOS_E_ESCALA.md` | Preparação para futuras reutilizações por outros afiliados | Diretriz de arquitetura |
| `06_LEIA_PRIMEIRO.md` | Resumo de uma página para humanos e IAs | Base V1 |
| `07_INDICE_E_STATUS.md` | Mapa da própria documentação | Atual |

## Pendências principais

### PENDÊNCIA 001 — Validação de feed/source

- validação estrutural;
- cabeçalhos;
- colunas obrigatórias;
- arquivo inválido/truncado;
- interrupção segura em caso de falha.

### PENDÊNCIA 002 — Atualização atômica de `ofertas.json`

- arquivo temporário;
- validação antes da troca;
- preservação da última versão válida.

### PENDÊNCIA 003 — Eliminar caminhos fixos/absolutos

- caminhos derivados do projeto;
- parametrização;
- execução consistente local/automática.

## Próximas decisões de negócio

1. aprovação formal da taxonomia V1;
4. aprovação formal da matriz de normalização V1;
5. definição do mecanismo/configuração de IDs estáveis das categorias;
6. desenho técnico do normalizador.
