# 🔒 cryptoML

**Privacy-Preserving Federated Learning Platform for Multi-Agency Cybersecurity Anomaly Detection**

![Docker](https://img.shields.io/badge/Docker-Enabled-blue) 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flower](https://img.shields.io/badge/Flower-Federated_Learning-green)

A secure, Docker-based platform that allows multiple agencies to collaboratively detect cyber threats **without sharing raw logs**.

---

## ✨ Features

- **True Federated Learning** — Train collaboratively using Flower + PyTorch
- **Strong Privacy** — Raw logs never leave their agency
- **Multi-Party Ready** — Simulate 2+ agencies with Docker Compose
- **Real Dataset Support** — Tested with Synthetic Cybersecurity Logs (Kaggle)
- **Interactive Dashboard** — Live metrics, anomalies, and audit logs via Streamlit
- **Anomaly Detection** — Autoencoder-based unsupervised learning
- **Audit Trail** — Basic logging (extendable to blockchain)

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/pranav-verma-daiict/cryptoML.git
cd cryptoML

# 2. Start the full system
docker compose -f .docker/docker-compose.yml up --build -d

# 3. Open the dashboard
open http://localhost:8501

## 📁 Project Structure
cryptoML/
├── .docker/                # Docker configurations
├── core/                   # Preprocessing & models
├── federation/             # Flower server & clients
├── dashboard/              # Streamlit UI
├── data/sample_logs/       # Real dataset (JSONL)
├── docs/                   # Full documentation
├── scripts/                # Utility scripts
└── README.md
```

## 🛠️ Tech Stack & Purpose

|     Component    |       Technology      |                  Purpose                  |
|:----------------:|:---------------------:|:-----------------------------------------:|
| ML Framework     | PyTorch + Flower      | Federated Learning orchestration          |
| Data Processing  | Pandas + Scikit-learn | Log standardization & feature engineering |
| Visualization    | Streamlit             | Real-time dashboard                       |
| Containerization | Docker + Compose      | Reproducible multi-agency environment     |
| Audit            | File-based logger     | Track training rounds                     |


## 🎯 Who Is This For?
- Cybersecurity teams wanting collaborative intelligence
- Researchers & students exploring Federated Learning in security
- Government / multi-organization environments with strict data sovereignty

## 🔍 MOAT & Competitive Edge
Unlike most open-source FL demos (toy datasets + single node), cryptoML delivers:
- Real cybersecurity log focus
- Production-like Docker multi-party simulation
- Working end-to-end MVP with real dataset validation

**Ready to contribute?** Feel free to open issues or PRs.
