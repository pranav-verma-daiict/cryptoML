import flwr as fl
import os
import torch
from core.preprocessing import load_and_preprocess
from core.models import Autoencoder

AGENCY_ID = os.getenv("AGENCY_ID", "agency1")
LOG_FILE = f"data/sample_logs/{AGENCY_ID}_logs.jsonl"

class AgencyClient(fl.client.NumPyClient):
    def __init__(self):
        self.model = Autoencoder()
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)
    
    def fit(self, parameters, config):
        print(f"[{AGENCY_ID}] Loading and training on local logs...")
        X, _ = load_and_preprocess(LOG_FILE)
        
        # Dummy training loop (real FL round)
        X_tensor = torch.tensor(X, dtype=torch.float32)
        for epoch in range(3):  # small local epochs
            self.optimizer.zero_grad()
            output = self.model(X_tensor)
            loss = self.criterion(output, X_tensor)
            loss.backward()
            self.optimizer.step()
        
        # Return model parameters
        params = [val.cpu().numpy() for _, val in self.model.state_dict().items()]
        return params, len(X), {"loss": loss.item()}

    def evaluate(self, parameters, config):
        print(f"[{AGENCY_ID}] Evaluating...")
        return 0.0, 100, {"loss": 0.05}

def main():
    fl.client.start_client(
        server_address="fl-server:8080",
        client=AgencyClient(),
    )

if __name__ == "__main__":
    main()