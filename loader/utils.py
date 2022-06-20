from utils import load_json, save_as_json


def add_post_by_list(new_post: dict) -> None:
    posts: list[dict] = load_json()
    posts.append(new_post)
    save_as_json(posts)
