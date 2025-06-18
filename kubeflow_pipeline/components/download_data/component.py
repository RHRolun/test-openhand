
import os
import requests
from kfp.components import OutputArtifact, create_component_link

def download_data(
    url: str,
) -> OutputArtifact('dataset'):
    """Download dataset from given URL"""
    response = requests.get(url)
    with open("demand_qty_item_loc.xlsx", "wb") as f:
        f.write(response.content)
    return OutputArtifact('dataset', 'demand_qty_item_loc.xlsx')

if __name__ == "__main__":
    download_data("https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx")
