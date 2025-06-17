
import os
import requests

def download_dataset():
    url = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
    response = requests.get(url)
    if response.status_code == 200:
        with open("demand_qty_item_loc.xlsx", "wb") as f:
            f.write(response.content)
        return "demand_qty_item_loc.xlsx"
    else:
        raise FileNotFoundError("Failed to download the dataset")

if __name__ == "__main__":
    download_dataset()
