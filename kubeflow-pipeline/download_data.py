

import os
import requests
import logging

def download_data(url: str, output_path: str) -> str:
    """Download data from URL and save to output path"""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Save the file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return output_path
        raise FileNotFoundError(f"Failed to download data from {url} with status code {response.status_code}")
    except Exception as e:
        raise RuntimeError(f"Error downloading data: {str(e)}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Download data from URL',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--url', type=str, required=True,
                       help='URL to download from (e.g. https://example.com/file.xlsx)')
    parser.add_argument('--output_path', type=str, required=True,
                       help='Full path to save the downloaded file (e.g. /data/file.xlsx)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.1')
    args = parser.parse_args()

    try:
        output = download_data(args.url, args.output_path)
        print(f"Data downloaded successfully to {output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Download failed: {str(e)}", exc_info=True)

