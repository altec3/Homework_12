from utils import load_json


def get_posts_by_substring(substring: str) -> list[dict] | None:
    posts: list[dict] = load_json()
    result = []
    for post in posts:
        content: str = post["content"]
        if substring.lower() in content.lower():
            result.append(post)
    return result
