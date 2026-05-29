import json
import os
from datetime import datetime

DATA_FILE = "keuangan.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            for index, item in enumerate(data):
                if "id" not in item:
                    item["id"] = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}_{index}"

                if "keterangan" not in item:
                    item["keterangan"] = ""

            return data
        except:
            return []

    return []


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)