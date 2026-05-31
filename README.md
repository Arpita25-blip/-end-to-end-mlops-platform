# -end-to-end-mlops-platform
# 🚀 End-to-End MLOps Platform

![CI/CD]![CI/CD](https://github.com/Arpita25-blip/-end-to-end-mlops-platform/actions/workflows/train.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326ce5?logo=kubernetes)
![MLflow](https://img.shields.io/badge/MLflow-Tracked-0194E2?logo=mlflow)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)

A production-grade, end-to-end MLOps pipeline featuring automated model training, CI/CD with GitHub Actions, containerization with Docker, deployment on Kubernetes (Minikube), and real-time monitoring with Prometheus + Grafana.

---

## 🏗️ Architecture

```
GitHub Push → GitHub Actions CI/CD → Docker Hub → Kubernetes (Minikube)
     ↓               ↓                                     ↓
  Code Lint     Train + Test                        FastAPI Model Serving
                MLflow Track                        Prometheus Metrics
                Docker Build                        Grafana Dashboard
                Docker Push                         Drift Detection
```

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| ML Framework | scikit-learn, pandas, numpy |
| Experiment Tracking | MLflow |
| Model Serving | FastAPI, Uvicorn |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus, Grafana |
| Drift Detection | Evidently AI |
| Testing | pytest |

---

## 📁 Project Structure

```
end-to-end-mlops-platform/
├── .github/workflows/
│   ├── train.yml          # CI: train & test on every push
│   └── deploy.yml         # CD: build & push Docker image
├── src/
│   ├── train.py           # Model training with MLflow logging
│   ├── evaluate.py        # Model evaluation & metrics
│   └── drift_detection.py # Data drift detection with Evidently
├── api/
│   └── app.py             # FastAPI model serving endpoint
├── k8s/
│   ├── deployment.yaml    # Kubernetes deployment
│   ├── service.yaml       # Kubernetes service
│   └── hpa.yaml           # Horizontal Pod Autoscaler
├── tests/
│   └── test_model.py      # Pytest unit tests
├── models/                # Saved model artifacts
├── reports/               # Drift detection reports
├── Dockerfile             # Container definition
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/end-to-end-mlops-platform
cd end-to-end-mlops-platform
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
```bash
python src/train.py
```

### 4. View experiments in MLflow
```bash
mlflow ui
# Open: http://localhost:5000
```

### 5. Run tests
```bash
pytest tests/ -v
```

### 6. Start API locally
```bash
uvicorn api.app:app --reload
# Open: http://localhost:8000/docs
```

### 7. Run with Docker
```bash
docker build -t e2e-mlops-platform .
docker run -p 8000:8000 e2e-mlops-platform
```

### 8. Deploy on Kubernetes
```bash
minikube start
kubectl apply -f k8s/
minikube service e2e-mlops-platform --url
```

---

## 📊 Key Results

- ✅ Model Accuracy: **97%+** on Wine dataset
- ✅ CI/CD pipeline runs automatically on every push
- ✅ Docker image auto-built and pushed to Docker Hub
- ✅ Kubernetes deployment with auto-scaling (HPA)
- ✅ Real-time metrics exposed via Prometheus
- ✅ Grafana dashboard for live monitoring
- ✅ Data drift detection reports via Evidently AI

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Project info |
| GET | `/health` | Health check |
| POST | `/predict` | Make prediction |
| GET | `/metrics` | Prometheus metrics |
| GET | `/docs` | Swagger UI |

---

## 👩‍💻 Author

**Arpita Jagadale** — SRE | DevOps | MLOps
- LinkedIn: linkedin.com/in/arpita-jagadale-a73a45216
- Email: arpitajagadale25@gmail.com
