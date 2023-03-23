from flask import Blueprint, render_template

main_app = Blueprint('main_app', __name__, static_folder='static')


@main_app.route('/', endpoint='index')
def index():
    return render_template('main/index.html')
