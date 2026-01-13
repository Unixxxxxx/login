
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


RUN python manage.py collectstatic --noinput || true


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
