from flask import Flask

from main.views import bp_main
from loader.views import bp_loader

app = Flask(__name__)

app.register_blueprint(bp_main)
app.register_blueprint(bp_loader)


if __name__ == "__main__":
    app.run()
