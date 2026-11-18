# AI381 Lab 2 – Bring Your Own Model

![CI](https://github.com/ramabawaaneh9/AI381-Lab2/actions/workflows/ci.yml/badge.svg?branch=main)

This project packages a machine learning churn prediction model as a tested FastAPI service running inside Docker.

## Run the service

Start the service with one command:

```bash
docker run -p 8000:8000 ghcr.io/ramabawaaneh9/ai381-lab2:f88d4cc0db6b0d7975b1be9132de19d0b0354b2f
```

Then open:

```text
http://localhost:8000/docs
```

## API Endpoints

### Health Check

```text
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

### Prediction

```text
POST /predict
```

Example request:

```json
{
  "tenure_months": 12,
  "monthly_fee": 45.5,
  "support_calls": 2,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic"
}
```

Example response:

```json
{
  "prediction": 0
}
```

## Tests

Run the tests locally with:

```bash
python -m pytest
```

The test suite checks:

- API health contract
- Model loading
- Valid prediction requests
- Input schema validation
- Deterministic predictions

## Docker

The project uses a multi-stage Docker build, runs as a non-root user, uses a pinned Python base image, and includes a Docker HEALTHCHECK.

## Continuous Integration

GitHub Actions automatically:

1. Runs linting with Ruff.
2. Runs the pytest test suite on pull requests.
3. Builds the Docker image on `main`.
4. Scans the image with Trivy.
5. Pushes the image to GitHub Container Registry with the commit SHA as the image tag.

## Container Image

Image tag:

```text
f88d4cc0db6b0d7975b1be9132de19d0b0354b2f
```

Image digest:

```text
sha256:e1d711fb7b6222e1d6e255167e9bca9f46c67ae9c2612abf497daa2ff715430d
```
