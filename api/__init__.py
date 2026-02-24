from flask import Flask

from api.routes.student_routes import students_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(students_bp)
    return app
