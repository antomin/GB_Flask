from flask import Blueprint, render_template

from blog.models import Article

main_app = Blueprint('main_app', __name__, static_folder='static')


@main_app.route('/', endpoint='index')
def index():
    new_articles = Article.query.order_by('created_at').limit(3)
    return render_template('main/index.html', new_articles=new_articles)
