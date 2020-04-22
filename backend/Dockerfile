FROM python:3.11-slim
WORKDIR /app
COPY backend/pyproject.toml ./
COPY backend/harbor ./harbor
RUN pip install --no-cache-dir .
EXPOSE 7200
CMD ["uvicorn", "harbor.api.app:app", "--host", "0.0.0.0", "--port", "7200"]
