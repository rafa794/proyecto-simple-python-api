FROM python:3.11
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=4 CMD curl -f http://localhost:8000/items || exit 1