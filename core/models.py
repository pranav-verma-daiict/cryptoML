import torch
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self, input_dim=5):   # Must match preprocessing
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
        )
        self.decoder = nn.Sequential(
            nn.Linear(8, 16),
            nn.ReLU(),
            nn.Linear(16, 32),
            nn.ReLU(),
            nn.Linear(32, input_dim)
        )
    
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

def get_model(input_dim=5):
    return Autoencoder(input_dim)

def detect_anomalies(model, X_tensor, threshold=0.5):
    model.eval()
    with torch.no_grad():
        reconstructed = model(X_tensor)
        mse = torch.mean((X_tensor - reconstructed)**2, dim=1)
    anomalies = mse > threshold
    return mse.numpy(), anomalies.numpy()
