# cryptoML

**Secure Multi-Agency Cybersecurity Log Sharing with Federated Learning**

Privacy-preserving platform for collaborative anomaly detection using Federated Learning. No raw logs are shared between agencies.

## Features (MVP - Week 1)
- Docker-based multi-party setup (simulated agencies)
- Standardized log ingestion
- Federated Learning with PyTorch + Flower (Autoencoder for anomalies)
- Basic Streamlit dashboard
- Strong privacy guarantees

## Quick Start

```bash
# Clone and run
git clone <your-repo-url>
cd cryptoML

# Start the system
docker compose -f .docker/docker-compose.yml up --build -d

# View dashboard
open http://localhost:8501
```

## Project Structure
See folder layout in docs/ or explore directly.

## Tech Stack
- Python 3.11, PyTorch, Flower
- Docker + Compose
- Streamlit

## Roadmap
- Week 1: Foundation (Done)
- Week 2: Enhanced FL + Preprocessing
- Week 3: Dashboard + Integration
- Week 4: Testing + Polish

**Privacy First**: Raw logs stay local. Only model updates shared.

---
Built following Project Bible v1.1 (Fast Track)