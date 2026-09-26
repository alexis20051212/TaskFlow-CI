
from flask import Flask, render_template, request, redirect, url_for


def create_app():
    app = Flask(__name__)

    tasks = []

    @app.route("/")
    def index():
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["POST"])
    def add_task():
        task_name = request.form.get("task", "").strip()

        if task_name:
            tasks.append(task_name)

        return redirect(url_for("index"))

    return app