from flask import Blueprint, render_template, request, send_from_directory
from loader.utils import add_post_by_list
import logging

logging.basicConfig(level=logging.ERROR)
logger_load = logging.getLogger("load")
file_handler = logging.FileHandler("img_load.log", encoding="utf-8")
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(formatter)
logger_load.addHandler(file_handler)

ALLOWED_EXTENSIONS = ["jpeg", "png"]

bp_loader = Blueprint("bp_loader", __name__, template_folder="templates")


@bp_loader.route("/post/", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@bp_loader.route("/post/", methods=["POST"])
def page_post_upload():
    file = request.files.get("picture")
    content: str = request.form.get("content")
    if file:
        filename = file.filename
        extension: str = filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            file.save(f"./uploads/images/{filename}")
            post: dict = {"pic": f"/uploads/images/{filename}", "content": content}
            add_post_by_list(post)
            return render_template("post_uploaded.html", new_post=post)
        else:
            logger_load.error(f"Не верный формат файла: .{extension}")
            # raise TypeError("Для загрузки разрешены только изображения .jpeg и .png")
            return f"<h3>Тип файлов .{extension} не поддерживается</h3>"
    else:
        # raise Exception("Не выбран файл для загрузки")
        return "<h3>Не выбран файл для загрузки.</h3>"


@bp_loader.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
