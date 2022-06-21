import json
from json import JSONDecodeError
import logging

logger_json = logging.getLogger("json")
file_handler = logging.FileHandler("load_json.log", encoding="utf-8")
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(formatter)
logger_json.addHandler(file_handler)

POSTS_LIST = "posts.json"


def load_json(path: str = POSTS_LIST) -> list[dict] | None:
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except JSONDecodeError as e:
            logger_json.warning(f"Не удается преобразовать файл {POSTS_LIST}")
            return None


def save_as_json(data: list[dict], path: str = POSTS_LIST) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print(load_json())
