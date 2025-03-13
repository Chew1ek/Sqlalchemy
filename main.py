from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user.surname = "NeScott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_ne_chief@mars.org"
    user.hashed_password = "no_cap"
    db_sess.add(user)
    db_sess.commit()

    user.surname = "AltScott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "alt_scott_chief@mars.org"
    user.hashed_password = "alt_cap"
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
