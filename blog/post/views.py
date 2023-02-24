from flask import Blueprint, render_template

from blog.user.views import USERS

post = Blueprint('post', __name__, url_prefix='/posts', static_folder='../static')

POSTS = {
    1: {
        'title': 'Статья №1',
        'text': 'Mauris ultrices vehicula nisl, ut finibus libero efficitur ac. Vivamus est nisi, condimentum nec'
                'tortor id, euismod interdum massa. Sed eros ex, rutrum eu tincidunt non, scelerisque at felis. Nam id'
                'nisi non lacus faucibus pretium. Pellentesque fermentum magna eros, egestas molestie urna consequat'
                'tempor. Maecenas sagittis vulputate pellentesque. Cras.',
        'author': 1,
        'created_at': '20.02.2021'
    },
    2: {
        'title': 'Статья №2',
        'text': 'Mauris ultrices vehicula nisl, ut finibus libero efficitur ac. Vivamus est nisi, condimentum nec'
                'tortor id, euismod interdum massa. Sed eros ex, rutrum eu tincidunt non, scelerisque at felis. Nam id'
                'nisi non lacus faucibus pretium. Pellentesque fermentum magna eros, egestas molestie urna consequat'
                'tempor. Maecenas sagittis vulputate pellentesque. Cras.',
        'author': 2,
        'created_at': '21.02.2021'
    },
    3: {
        'title': 'Статья №3',
        'text': 'Mauris ultrices vehicula nisl, ut finibus libero efficitur ac. Vivamus est nisi, condimentum nec'
                'tortor id, euismod interdum massa. Sed eros ex, rutrum eu tincidunt non, scelerisque at felis. Nam id'
                'nisi non lacus faucibus pretium. Pellentesque fermentum magna eros, egestas molestie urna consequat'
                'tempor. Maecenas sagittis vulputate pellentesque. Cras.',
        'author': 3,
        'created_at': '22.02.2021'
    },
}


@post.route('/')
def post_list():
    return render_template('post/list.html', users=USERS, posts=POSTS)


@post.route('/<int:pk>')
def past_detail(pk: int):
    post = POSTS[pk]
    user = USERS[post['author']]
    return render_template('post/detail.html', user=user, post=post)