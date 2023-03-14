import datetime

from flask import Flask, render_template
from data import db_session
from data.users import User, Jobs
from data.news import News


app = Flask(__name__)
app.config['SECRET_KEY'] = '43k4jb6jb5k42k422o0obg44d9f10nf'


def main():
    db_session.global_init('db/blogs.db')
    app.run(debug=True)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    data = db_sess.query(Jobs).all()
    for elem in data:
        user = db_sess.query(User).filter(User.id == elem.team_leader).first()
        elem.team_leader = user.surname + ' ' + user.name
    db_sess.close()
    return render_template('main.html', data=(data, len(data)))


if __name__ == '__main__':
    main()