from pathlib import Path

# Определяем путь до csv-файла с данными
ROOT = Path(__file__).resolve().parent
SRC_PATH = Path.joinpath(ROOT, 'src')
DATA_PATH = Path.joinpath(SRC_PATH, 'items.csv')