
import kfp
from kfp import dsl

@kfp.dsl.component
def download_data(url: str) -> str:
    """Download data component."""
    return kfp.dsl.ContainerOp(
        name='download_data',
        image='alpine:3.18',
        command=['sh', '-c', 'wget -O /tmp/data.xlsx "$0" && echo "/tmp/data.xlsx"'],
        arguments=[url]
    ).output

@kfp.dsl.component
def train_model(data_path: str) -> str:
    """Train model component."""
    return kfp.dsl.ContainerOp(
        name='train_model',
        image='python:3.10',
        command=['sh', '-c', 'python train_model.py "$0" && echo "model.pkl"'],
        arguments=[data_path]
    ).output
