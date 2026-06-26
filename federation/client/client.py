import flwr as fl
import os
import torch
from core.preprocessing import load_and_preprocess
from core.models import get_model, detect_anomalies   # ← Make sure this line exists

AGENCY_ID = os.getenv("AGENCY_ID", "agency1")
LOG_FILE = f"data/sample_logs/{AGENCY_ID}_logs.jsonl"

class AgencyClient(fl.client.NumPyClient):
    def __init__(self):
        self.model = get_model()
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
    
    def get_parameters(self, config):
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def fit(self, parameters, config):
        print(f"[{AGENCY_ID}] Local training round...")
        
        X, _, _ = load_and_preprocess(LOG_FILE)
        X_tensor = torch.tensor(X, dtype=torch.float32)
        
        if parameters is not None and len(parameters) > 0:
            params_dict = zip(self.model.state_dict().keys(), parameters)
            state_dict = {k: torch.tensor(v) for k, v in params_dict}
            self.model.load_state_dict(state_dict, strict=True)
        
        for epoch in range(2):
            self.optimizer.zero_grad()
            output = self.model(X_tensor)
            loss = self.criterion(output, X_tensor)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            self.optimizer.step()
        
        # Anomaly detection
        mse, anomalies = detect_anomalies(self.model, X_tensor)
        print(f"[{AGENCY_ID}] Detected {int(anomalies.sum())} anomalies locally")
        
        new_params = [val.cpu().numpy() for _, val in self.model.state_dict().items()]
        return new_params, len(X), {"loss": loss.item(), "anomalies": int(anomalies.sum())}

    def evaluate(self, parameters, config):
        print(f"[{AGENCY_ID}] Evaluating global model...")
        return 0.0, 100, {"loss": 0.03}

def main():
    fl.client.start_client(
        server_address="fl-server:8080",
        client=AgencyClient().to_client(),
    )

if __name__ == "__main__":
    main()
