from flask import render_template, request, Blueprint
from app.models import Post
from flask_login import login_required
main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
@login_required
def home():
    page = request.args.get('page',1,type = int)
    # posts = Post.query.paginate(page=page ,per_page = 10)
    posts = Post.query.order_by(Post.id.desc()).paginate(page=page ,per_page = 3)

    return render_template('home.html',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')
