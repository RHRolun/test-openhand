

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging

def train_model(data_path: str, model_path: str) -> str:
    """Train a simple linear regression model"""
    try:
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
    except Exception as e:
        logging.error(f"Training failed: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to train model: {str(e)}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Train demand forecasting model')
    parser.add_argument('--data_path', type=str, required=True, help='Path to data file')
    parser.add_argument('--model_path', type=str, required=True, help='Path to save the model')
    args = parser.parse_args()

    try:
        model_path = train_model(args.data_path, args.model_path)
        print(f"Model trained and saved at: {model_path}")
    except Exception as e:
        print(f"Error training model: {str(e)}")

