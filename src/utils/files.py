import json
from pathlib import Path

# Project root: relative-r/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def add_to_json(key, data, filename):
    file_path = DATA_DIR / f"{filename}.json"

    try:
        with open(file_path, "r") as f:
            file_data = json.load(f)
            
    except (json.JSONDecodeError, FileNotFoundError):
        file_data = {}

    file_data[key] = data

    with open(file_path, "w") as f:
        json.dump(file_data, f, indent=2)

def get_ticker_symbol(
        min_volume: int | None = None, #100000,
        min_price: float | None = None, #1.0,
        max_price: float | None = None, #20,

    ) -> list[str]:
    file_path = DATA_DIR / "assets.json"

    with open(file_path, "r") as f:
        file_data = json.load(f)

    ticker_symbols = list(file_data.keys())

    if min_volume:
        ticker_symbols = [ticker for ticker in ticker_symbols if file_data[ticker]["last_volume"] >= min_volume]

    if min_price:
        ticker_symbols = [ticker for ticker in ticker_symbols if file_data[ticker]["previous_close"] >= min_price]

    if max_price:
        ticker_symbols = [ticker for ticker in ticker_symbols if file_data[ticker]["previous_close"] <= max_price]

    return ticker_symbols
