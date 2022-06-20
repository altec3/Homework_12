import json
POSTS_LIST = "posts.json"


def load_json(path: str = POSTS_LIST) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_as_json(data: list[dict], path: str = POSTS_LIST) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print(load_json())
