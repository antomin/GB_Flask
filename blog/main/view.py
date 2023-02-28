from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='static')


@main.route('/', endpoint='index')
def index():
    return render_template('main/index.html')
