from flask import render_template, Flask

app = Flask(__name__)

# <h1>{{ username }}的个人主页</h1>
# {% if bio %}
#     <p>{{ bio }}</p>  {# 这里的缩进只是为了可读性，不是必须的 #}
# {% else %}
#     <p>自我介绍为空。</p>
# {% endif %}  {# 大部分 Jinja 语句都需要声明关闭 #}

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/home')
def hello():
    return 'hello'
