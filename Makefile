# Makefile for Customer Churn Prediction API (with conda support)

ENV_NAME=churn-env

.PHONY: install run train test lint docker-build docker-run clean

install-dev:
	conda run -n $(ENV_NAME) pip install -r requirements/dev.txt

install-prod:
	conda run -n $(ENV_NAME) pip install -r requirements/prod.txt

run:
	conda run -n $(ENV_NAME) uvicorn app.main:app --reload

# train:
# 	conda run -n $(ENV_NAME) python notebooks/train_model.py

# test:
# 	conda run -n $(ENV_NAME) pytest tests/

lint:
	conda run -n $(ENV_NAME) black app/ --check
	conda run -n $(ENV_NAME) isort app/ --check-only

format:
	conda run -n $(ENV_NAME) black app/
	conda run -n $(ENV_NAME) isort app/

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	docker build -t customer-churn-prediction-api .

docker-run:
	docker run -d -p 8000:8000 customer-churn-prediction-api:latest

docker-tag:
	docker image tag customer-churn-prediction-api:latest jagadish9084/customer-churn-prediction-api:latest

docker-push:
	docker push jagadish9084/customer-churn-prediction-api:latest


# Kubernetes deployment section
.PHONY: k8s-deploy k8s-delete k8s-logs k8s-status

# Apply all Kubernetes manifests
k8s-deploy:
	kubectl apply -f manifests/

# Delete all Kubernetes resources
k8s-delete:
	kubectl delete -f manifests/

# Check status of pods and services
k8s-status:
	kubectl get pods -o wide
	kubectl get svc

# View logs from the churn-api container
k8s-logs:
	kubectl logs -l app=customer-churn-prediction-api --tail=100 -f
