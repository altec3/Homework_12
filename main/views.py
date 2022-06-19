from flask import Blueprint, render_template, request, escape
from main.utils import get_posts_by_substring

bp_main = Blueprint("bp_main", __name__, template_folder="templates")


@bp_main.route("/")
def main_page():
    return render_template("index.html")


@bp_main.route("/search/")
def search_page():
    target = request.args.get("s")
    if target:
        posts: list[dict] = get_posts_by_substring(escape(target))
        return render_template("post_list.html", target=target, posts=posts)
    else:
        return "<h1>Вы ничего не ввели в поле поиска</h1>"
