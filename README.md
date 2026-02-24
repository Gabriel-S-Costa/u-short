# Objetivo

Desenvolver uma API para gerenciar links curtos. Utilizando as melhores práticas de arquitetura de software, com foco em DDD e Clean Architecture.

## Tecnologias

- Python 3.14
- FastAPI
- Uv
- Ruff
- Pydantic
- Alembic
- SQLModel

## Estrutura do projeto

```
app/
├── core/
│   ├── database.py
│   └── security.py
├── modules/
│   ├── accounts/
│   │   ├── application/
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   └── presentation/
│   ├── links/
│   │   ├── application/
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   └── presentation/
│   └── analytics/
│       ├── application/
│       ├── domain/
│       ├── infrastructure/
│       └── presentation/
├── main.py
└── routers/
    ├── accounts.py
    ├── links.py
    └── analytics.py
```

