# 📉 Customer Churn Prediction API

A production-ready machine learning API that predicts whether a customer is likely to churn. Built using **FastAPI**, containerized with **Docker**, and deployed via **Kubernetes**.

---

## 🚀 Features

- 🧑‍🎓 Predicts customer churn using a trained ML model
- ⚡ Built with FastAPI for high performance and easy API integration
- 🐳 Dockerized for easy packaging and deployment
- ☘️ Kubernetes-ready for scalable deployment
- 🔍 Lightweight and easy to test locally or on the cloud

---

## 📁 Project Structure

```
customer-churn-prediction-api/
│
├── app/
│   ├── main.py                      # FastAPI app entry
│   ├── models/                      # Saved ML model (.h5)
│   │   └── model.h5
│   ├── routes/                      # Route declarations
│   │   ├── __init__.py
│   │   └── request_model.py
│   ├── schemas/                     # Pydantic models
│   │   ├── __init__.py
│   │   └── request_model.py
│   ├── services/                    # Prediction logic
│   │   ├── __init__.py
│   │   └── prediction_service.py
│   ├── utils/                       # Encoders and scaler files
│   │   ├── label_encoder_gender.pkl
│   │   ├── on_hot_encoder_geography.pkl
│   │   └── scalar.pkl
│   └── __init__.py
│
├── notebooks/
│   └── experiment_notebook.ipynb   # Model development notebook
│
├── Dockerfile                      # Docker build config
├── .dockerignore                   # Docker ignore rules
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── deployment.yaml                 # Kubernetes Deployment
└── service.yaml                    # Kubernetes Service
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the repo
```bash
git clone https://github.com/jagadish9084/customer-churn-prediction-api.git
cd customer-churn-prediction-api
```

### ✅ 2. Install dependencies (for local testing)
```bash
pip install -r requirements.txt
```

### ✅ 3. Run the API locally
```bash
uvicorn app.main:app --reload
```
Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Docker Usage

### ✅ Build Docker image
```bash
docker build -t customer-churn-prediction-api .
```

### ✅ Run Docker container
```bash
docker run -d -p 8000:8000 customer-churn-prediction-api
```

---

## ☘️ Deploy on Kubernetes

### ✅ Build the image inside Minikube
```powershell
& minikube docker-env | Invoke-Expression
docker build -t customer-churn-prediction-api:latest .
```

### ✅ Apply K8s manifests
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### ✅ Access your service
```bash
minikube service churn-api-service
```

---

## 📆 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/predict`       | Predicts churn status    |
| GET    | `/health`        | Health check             |
| GET    | `/docs`          | Interactive Swagger UI   |

---

## 🧑‍🎓 Model Info

- Algorithm: *e.g., ANN
- Training dataset: *Provide name or description*
- Metrics: *Accuracy, Precision, Recall, F1-score*

---

## 🛡️ Future Improvements(TODO)

- ✅ Add CI/CD with GitHub Actions
- ✅ Load testing with Locust
- ✅ Logging and monitoring (Prometheus + Grafana)
- ✅ Ingress & TLS support

---

## 👨‍💼 Author

**Jagadish Sonamale**  
🔗 [LinkedIn](https://www.linkedin.com/in/jagadishsonamale)  
📧 jagadish9084@gmail.com

---

## 📂 License

This project is licensed under the MIT License.

