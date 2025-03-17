from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(input())
    # app.run()
    user = User()

    db_sess = db_session.create_session()
    db_sess.commit()

    for i in db_sess.query(User).all():
        print(f'<Colonist> {i.id} {i.surname} {i.name}')


if __name__ == '__main__':
    main()
