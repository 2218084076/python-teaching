"""
files operations
"""
import csv
import datetime
import os
from pathlib import Path
from typing import List

from cralwers.config import settings


def write_to_file(info: List[dict], file_name: str):
    """
    write to file
    """
    keys = info[0].keys()
    out_put_path = Path(__file__).parent.parent.parent / settings.OUTPUT_DATA_DIR
    os.makedirs(out_put_path, exist_ok=True)
    with open(
            Path(out_put_path, f'{file_name}-{datetime.datetime.now().date()}.csv'),
            'w', newline='', encoding='utf-8'
    ) as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(info)
