# Delivery Service

API сервис для управления доставкой.

## Установка

1. Установите Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Установите зависимости:
```bash
poetry install
```

3. Установите pre-commit хуки:
```bash
poetry run pre-commit install
```

## Запуск

### Локально

```bash
poetry run uvicorn delivery_service.main:app --reload
```

### С использованием Docker

```bash
docker-compose up --build
```

## Тестирование

```bash
poetry run pytest
```

## Структура проекта

```
delivery_service/
├── src/
│   └── delivery_service/
│       ├── api/         # API эндпоинты
│       ├── core/        # Основная логика
│       ├── db/          # Работа с базой данных
│       ├── models/      # Модели данных
│       └── schemas/     # Pydantic схемы
├── tests/              # Тесты
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```