# Makefile for Customer Churn Prediction API (with conda support)

ENV_NAME=churn-env

.PHONY: install run train test lint docker-build docker-run clean

install:
	conda run -n $(ENV_NAME) pip install -r requirements.txt

run:
	conda run -n $(ENV_NAME) uvicorn app.main:app --reload

train:
	conda run -n $(ENV_NAME) python notebooks/train_model.py

test:
	conda run -n $(ENV_NAME) pytest tests/

lint:
	conda run -n $(ENV_NAME) black app/ --check
	conda run -n $(ENV_NAME) isort app/ --check-only

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	docker build -t churn-api .

docker-run:
	docker run -d -p 8000:8000 churn-api
