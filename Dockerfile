FROM python:3.11-slim

WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем исходный код
COPY . .

# Запускаем приложение
CMD ["poetry", "run", "uvicorn", "delivery_service.main:app", "--host", "0.0.0.0", "--port", "8000"] 