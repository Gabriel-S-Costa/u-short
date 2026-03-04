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
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── app/
│   ├── core/
│   │   ├── database.py
│   │   └── security.py
│   ├── modules/
│   │   ├── accounts/
│   │   │   ├── application/
│   │   │   ├── domain/
│   │   │   ├── infrastructure/
│   │   │   └── presentation/
│   │   ├── links/
│   │   │   ├── application/
│   │   │   ├── domain/
│   │   │   ├── infrastructure/
│   │   │   └── presentation/
│   │   └── analytics/
│   │       ├── application/
│   │       ├── domain/
│   │       ├── infrastructure/
│   │       └── presentation/
│   ├── main.py
│   └── routers/
│       ├── accounts.py
│       ├── links.py
│       └── analytics.py
├── alembic.ini
└── pyproject.toml
```

## Migrations (Alembic)

Este projeto utiliza o **Alembic** acoplado ao `SQLModel` para gerenciar as versões do banco de dados (migrations), com as migrations fixadas na raiz do projeto.

Para o Alembic reconhecer os modelos das suas tabelas corretamente de forma automática, lembre-se de importar a sua nova model dentro de `alembic/env.py`.

### Comandos Principais

- **Gerar uma migration automaticamente (autogenerate):**
  ```bash
  alembic revision --autogenerate -m "descrição_da_sua_mudança"
  ```
  Isso irá comparar a estrutura definida nos seus arquivos `SQLModel` com a estrutura atual do banco de dados e criará um novo script em `alembic/versions/`.

- **Aplicar as migrations pendentes no banco de dados:**
  ```bash
  alembic upgrade head
  ```

- **Reverter a última migration aplicada:**
  ```bash
  alembic downgrade -1
  ```
