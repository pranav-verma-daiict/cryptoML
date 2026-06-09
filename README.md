# cryptoML

**Secure Multi-Agency Cybersecurity Log Sharing with Federated Learning**

## Problem Statement

Organizations and cybersecurity agencies often operate in silos, unable to effectively share security intelligence due to privacy and confidentiality concerns. Centralized log aggregation raises critical data governance issues—no single party should have access to all agencies' raw security logs. This fragmentation hampers collaborative threat detection and incident response.

## Solution

cryptoML implements a **privacy-preserving platform for collaborative anomaly detection** using Federated Learning. Agencies train machine learning models locally on their own logs without sharing raw data. Only encrypted model updates are exchanged and aggregated to build a global model. This approach:

- ✅ **Preserves Privacy**: Raw logs remain local and confidential
- ✅ **Enables Collaboration**: Agencies collectively learn from shared patterns
- ✅ **Maintains Autonomy**: Each agency retains full control over its data
- ✅ **Scales Efficiently**: Decentralized model training and aggregation

## Key Features

- **Federated Learning Architecture**: Uses Flower framework for distributed model training
- **Autoencoder-Based Anomaly Detection**: Identifies unusual patterns in security logs
- **Multi-Agency Simulation**: Docker-based setup for testing with multiple agencies
- **Real-time Dashboard**: Streamlit interface for monitoring anomalies and FL rounds
- **Standardized Log Processing**: JSON-based log schema with preprocessing pipeline
- **Cryptographic Security**: Integration-ready for secure model aggregation

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **ML Framework** | PyTorch 2.4.0 |
| **Federated Learning** | Flower (flwr) 1.13.0 |
| **Data Processing** | Pandas, NumPy, scikit-learn |
| **Dashboard** | Streamlit 1.38.0 |
| **Containerization** | Docker & Docker Compose |
| **Security** | Cryptography library |
| **Language** | Python 3.11 |

## Directory Structure

```
cryptoML/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── config/                            # Configuration files
│   ├── settings.yaml                 # Federation and privacy settings
│   └── log_schema.json               # Log data schema definition
├── core/                             # Core ML modules
│   ├── models.py                     # Autoencoder model definition
│   ├── preprocessing.py              # Log preprocessing pipeline
│   └── __init__.py
├── federation/                       # Federated Learning components
│   ├── server/
│   │   ├── server.py                # FL server (aggregator)
│   │   └── __init__.py
│   ├── client/
│   │   ├── client.py                # FL client (agency)
│   │   └── __init__.py
│   └── __init__.py
├── dashboard/                        # Web UI
│   ├── app.py                       # Streamlit dashboard
│   └── __init__.py
├── data/                            # Data directory
│   └── sample_logs/
│       ├── agency1_logs.jsonl       # Sample logs from agency 1
│       └── agency2_logs.jsonl       # Sample logs from agency 2
└── audit/                           # Audit logging
    ├── audit_logger.py              # Event audit trail
    └── __init__.py
```

### Directory Descriptions

- **config/**: Configuration files for federation settings, privacy parameters (differential privacy epsilon, gradient clipping), and standardized log schema
- **core/**: Core machine learning components including the Autoencoder model for anomaly detection and the preprocessing pipeline
- **federation/**: Federated learning orchestration with server (aggregator) and client (agency) implementations
- **dashboard/**: Web-based monitoring interface built with Streamlit for real-time visualization
- **data/**: Sample JSONL log files for testing and demonstration
- **audit/**: Audit logging for tracking all system events and operations

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git
- Python 3.11+ (for local development)

### Running the System

1. **Clone the repository**
   ```bash
   git clone https://github.com/pranav-verma-daiict/cryptoML.git
   cd cryptoML
   ```

2. **Install dependencies** (optional, for local development)
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the federated learning system**
   ```bash
   docker compose -f .docker/docker-compose.yml up --build -d
   ```

4. **Access the dashboard**
   ```
   Open http://localhost:8501 in your browser
   ```

5. **View logs** (optional)
   ```bash
   docker compose -f .docker/docker-compose.yml logs -f
   ```

6. **Stop the system**
   ```bash
   docker compose -f .docker/docker-compose.yml down
   ```

## Log Schema

Logs are stored in JSONL format with the following structure:

```json
{
  "timestamp": "2026-06-06T08:00:00",
  "source_ip": "192.168.1.10",
  "dest_ip": "10.0.0.5",
  "event_type": "login",
  "log_level": "INFO",
  "message": "Successful login",
  "user_id": "user1",
  "process_id": 1001
}
```

Refer to `config/log_schema.json` for the complete schema definition.

## Configuration

Edit `config/settings.yaml` to customize:

- **Federation Parameters**: Server address, number of rounds, minimum clients
- **Privacy Settings**: Differential privacy epsilon, gradient clipping norm
- **Log Schema Fields**: Specify which log fields to process

## Development Workflow

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FL server
python federation/server/server.py

# In another terminal, run a client
AGENCY_ID=agency1 python federation/client/client.py

# In another terminal, run the dashboard
streamlit run dashboard/app.py
```

### Adding New Agencies

1. Create sample logs in `data/sample_logs/{agency_name}_logs.jsonl`
2. Update Docker Compose to include a new service for the agency
3. Set the `AGENCY_ID` environment variable to your agency name

## Security Considerations

- **Privacy**: Only model updates (gradients) are shared, never raw logs
- **Encryption**: Integrate secure aggregation protocols for gradient encryption
- **Audit Trail**: All operations logged in `data/audit.log` for compliance
- **Access Control**: Implement authentication for dashboard and federation server

## Future Enhancements

- Differential privacy mechanisms for gradient perturbation
- Secure multi-party computation for aggregation
- Enhanced anomaly detection models (LSTM, GRU)
- Advanced visualization and alerting
- Multi-round model persistence and recovery

## Contributing

Contributions are welcome. Please ensure code follows Python best practices and includes appropriate documentation.

## License

[Add your license information here]

## Contact

For questions or issues, please open an issue on GitHub.
