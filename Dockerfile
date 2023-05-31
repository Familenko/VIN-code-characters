# Використання базового образу Python
FROM python:3.10

# Встановлення залежностей
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копіювання всього вмісту поточної папки до контейнера
COPY . /app

# Визначення аргументу командного рядка
ARG INPUT_DIR

# Запуск скрипту при старті контейнера з передачею аргументу командного рядка
CMD ["python", "inference.py", "--input", "$INPUT_DIR"]
