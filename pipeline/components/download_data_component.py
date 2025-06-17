
def download_data_component():
    """Download the demand quantity data from GitHub"""
    from kfp.components import InputPath, OutputPath
    import requests
    import os

    @kfp.dsl.component
    def download_data(
        output_data_path: OutputPath("ExcelFile"),
    ):
        """Download data from GitHub and save it locally"""
        url = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
        response = requests.get(url)
        with open(os.path.join(output_data_path.path, "demand_data.xlsx"), "wb") as f:
            f.write(response.content)

    return download_data
