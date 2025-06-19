
import os
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def download_data(url: str, output_path: str) -> str:
    """Download data from URL and save to output path"""
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return output_path
    raise FileNotFoundError(f"Failed to download data from {url}")

def train_model(data_path: str, model_path: str) -> str:
    """Train a simple linear regression model"""
    # Read data
    df = pd.read_excel(data_path)

    # Simple feature engineering - assuming we're predicting 'demand_qty'
    X = df[['item_loc']]
    y = df['demand_qty']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    pd.Series(model.coef_).to_csv(model_path, header=False)

    return model_path

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Kubeflow Pipeline for Demand Forecasting')
    parser.add_argument('--url', type=str, required=True, help='URL to download data from')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the file')
    parser.add_argument('--model_path', type=str, required=True, help='Path to save the model')
    args = parser.parse_args()

    # Download data
    data_path = download_data(args.url, args.output_path)

    # Train model
    train_model(data_path, args.model_path)
