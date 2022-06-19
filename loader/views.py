from flask import Blueprint, render_template, request, send_from_directory
from loader.utils import add_post_by_list

bp_loader = Blueprint("bp_loader", __name__, template_folder="templates")


@bp_loader.route("/post/", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@bp_loader.route("/post/", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content: str = request.form.get("content")
    if picture:
        filename = picture.filename
        picture.save(f"./uploads/images/{filename}")
        post: dict = {"pic": f"./uploads/images/{filename}", "content": content}
        add_post_by_list(post)
        return render_template("post_uploaded.html", new_post=post)
    else:
        return "<h3>Не выбран файл для загрузки.</h3>"


@bp_loader.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
