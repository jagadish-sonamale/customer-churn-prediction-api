# 📉 Customer Churn Prediction API

A production-ready, containerized REST API built with **FastAPI** that predicts customer churn using a trained machine learning model. Designed for real-world deployments with Docker, Kubernetes, and CI/CD readiness.

---

## 🚀 Features

- ✅ Fast and lightweight **TFLite model** for inference
- 📆 Packaged with **FastAPI** for blazing-fast REST endpoints
- 🧠 Predicts customer churn probability in real time
- 🧪 Modular structure with preloaded model, encoders, and scaler
- 🐳 Containerized with **Docker** and ready for **Kubernetes**
- 🧰 Integrated formatting (`black`, `isort`) and testing (`pytest`) support
- 📄 Uses `Makefile` for environment-agnostic, repeatable developer workflows

---

## 🧠 Why TFLite?

We use **TensorFlow Lite (TFLite)** for inference instead of a full `.h5` or `SavedModel` format because:

- ⚡ **Performance:** TFLite is optimized for speed and low memory consumption, especially useful in production APIs
- 🧱 **Lightweight:** Reduces the model size significantly (ideal for Docker images, CI/CD pipelines, edge devices)
- 🐍 **Easy Integration:** Works seamlessly with Python via the `tf.lite.Interpreter`
- 🚀 **Faster cold start** times in containerized environments

This makes it ideal for running fast, server-side predictions in a scalable, production-grade ML API.

---

## 🎛 Why Use a Makefile?

The `Makefile` allows us to automate common project tasks using simple, memorable commands without worrying about long bash scripts or remembering individual flags. It makes the development workflow consistent and easy to onboard across teams.

**Examples of what it simplifies:**

- Running the API server: `make run`
- Training the model: `make train`
- Installing environment-specific dependencies: `make install-dev` or `make install-prod`
- Linting and formatting: `make lint` / `make format`
- Deploying to Kubernetes: `make k8s-deploy`

This ensures a reproducible development environment and avoids human error.

---

## 📥 Setup Instructions

Follow the steps below to set up the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jagadish9084/customer-churn-prediction-api.git
cd customer-churn-prediction-api
```

### 2️⃣ Create and activate Conda environment
```bash
conda create -n churn-env python=3.9 -y
conda activate churn-env
```

### 3️⃣ Install development dependencies
```bash
make install-dev
```

### 4️⃣ Run the FastAPI application
```bash
make run
```

Visit: http://localhost:8000/docs to access the interactive Swagger API UI.

---

## 📂 Project Structure

```
customer-churn-prediction-api/
├── app/                  # FastAPI app with routes, models, services
│   ├── main.py
│   ├── routes/
│   ├── models/
│   ├── schemas/
├── models/               # Trained ML artifacts (TFLite model, encoders, scaler)
├── manifests/            # Kubernetes manifests
├── requirements/         # Pip requirement files for dev/prod
├── Dockerfile            # Production Docker image
├── Makefile              # Dev + deployment automation
├── .dockerignore
└── README.md
```

---

## ⚙️ Makefile Commands

```bash
make install-dev        # Install development dependencies
make install-prod       # Install production dependencies
make run                # Run FastAPI app with uvicorn
make train              # Train your model (edit this to fit your path)
make lint               # Run black and isort to check code formatting
make format             # Auto-format code with black and isort
make test               # Run all unit tests with pytest
make clean              # Remove __pycache__ and .pyc files
make docker-build       # Build Docker image
make docker-run         # Run Docker container
make k8s-deploy         # Apply all Kubernetes manifests
make k8s-delete         # Delete all Kubernetes resources
make k8s-status         # Show status of pods and services
make k8s-logs           # Tail logs from churn-api pods
```

---

## ⚙️ API Endpoint

### `POST /api/v1/predict`

**Request:**

```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Male",
  "Age": 35,
  "Tenure": 5,
  "Balance": 60000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000.0
}
```

**Response:**

```json
{
  "churn_probability": 0.75
}
```

---

## 🐳 Docker Usage

### 🔧 Build the image:

```bash
docker build -t churn-api .
```

### ▶️ Run the container:

```bash
docker run -d -p 8000:8000 churn-api
```

### 🧼 Stop and remove container:

```bash
docker ps                    # Get container ID
docker stop <container_id>
docker rm <container_id>
```

### 🧪 Test the running API:

Open browser or use curl:
```bash
curl http://localhost:8000/docs
```

---

## ☘️ Kubernetes Deployment

### Apply all manifests:
```bash
kubectl apply -f manifests/
```

### Check status:
```bash
kubectl get pods
kubectl get svc
```

### View logs:
```bash
kubectl logs -l app=churn-api -f
```

### Delete all Kubernetes resources:
```bash
kubectl delete -f manifests/
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

- Algorithm: *e.g., ANN*
- Training dataset: *Provide name or description*
- Metrics: *Accuracy, Precision, Recall, F1-score*

---

## 🛡️ Future Improvements(TODO)

- ✅ Add CI/CD with GitHub Actions
- ✅ Load testing with Locust
- ✅ Logging and monitoring (Prometheus + Grafana)
- ✅ Ingress & TLS support

---

## 🙇‍♂️ Author

**Jagadish Sonamale**  
Backend Architect | ML Enthusiast  
📧 jagadish.sonamale@gmail.com  
🔗 [GitHub](https://github.com/jagadish-sonamale) | [LinkedIn](https://www.linkedin.com/in/jagadish-sonamale/)

---

## 🧠 License

This project is licensed under the MIT License.