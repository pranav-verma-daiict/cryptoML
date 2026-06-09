import flwr as fl

def main():
    strategy = fl.server.strategy.FedAvg(
        min_fit_clients=2,
        min_available_clients=2,
    )
    
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=5),
        strategy=strategy,
    )

if __name__ == "__main__":
    main()