from dataclasses import dataclass


@dataclass(frozen=True)
class RegraClassificacao:
    """Representa uma regra declarativa de classificação."""

    id: str
    prioridade: int
    categoria: str
    subcategoria: str | None
    inclui: tuple[str, ...] = ()
    apoios: tuple[str, ...] = ()
    exclui: tuple[str, ...] = ()
