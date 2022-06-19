from flask import Flask, request, render_template, send_from_directory
# from functions import ...

from main.views import bp_main
from loader.views import bp_loader

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(bp_main)
app.register_blueprint(bp_loader)


if __name__ == "__main__":
    app.run()
