# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY .app/ .

# Открываем порт
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "run.py"]