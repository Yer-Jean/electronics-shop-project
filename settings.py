from pathlib import Path

# Определяем путь до csv-файла с данными
DATA_FILE = 'items.csv'
ROOT = Path(__file__).resolve().parent
SRC_PATH = Path.joinpath(ROOT, 'src')
DATA_PATH = Path.joinpath(SRC_PATH, DATA_FILE)