from flask import Blueprint, render_template, request, escape
import logging

from main.utils import get_posts_by_substring

logging.basicConfig(level=logging.INFO)
logger_main = logging.getLogger("main")
file_handler = logging.FileHandler("search.log", encoding="utf-8")
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(formatter)
logger_main.addHandler(file_handler)

bp_main = Blueprint("bp_main", __name__, template_folder="templates")


@bp_main.route("/")
def main_page():
    return render_template("index.html")


@bp_main.route("/search/")
def search_page():
    target = request.args.get("s")
    logger_main.info(f"Запрос на поиск подстроки: \"{target}\"")
    if target:
        posts: list[dict] = get_posts_by_substring(escape(target))
        return render_template("post_list.html", target=target, posts=posts)
    else:
        return "<h1>Вы ничего не ввели в поле поиска</h1>"
