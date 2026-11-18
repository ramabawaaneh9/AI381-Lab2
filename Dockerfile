
FROM python:3.12.3-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12.3-slim

WORKDIR /app

RUN useradd --create-home appuser

COPY --from=builder /install /usr/local

COPY src ./src

# Lab 3: Use the promoted champion model
COPY artifacts/model.joblib ./model.joblib
COPY artifacts/metadata.json ./artifacts/metadata.json

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')" || exit 1

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
