import requests
from flask import Blueprint, render_template

from blog.models import Article

main_app = Blueprint('main_app', __name__, static_folder='static')


@main_app.route('/', endpoint='index')
def index():
    # new_articles = Article.query.order_by('created_at').limit(3)
    response = requests.get('http://127.0.0.1:5000/api/articles/')
    json_articles = response.json()
    new_articles = json_articles.get('data')
    return render_template('main/index.html', new_articles=new_articles)
