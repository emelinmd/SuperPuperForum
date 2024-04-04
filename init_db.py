# init_db.py
from server import app
from extensions import db
from models import Section

with app.app_context():
    db.create_all()


def add_sections():
    with app.app_context():
        new_section = Section(title='Новый раздел', description='Описание нового раздела')
        db.session.add(new_section)
        db.session.commit()


if __name__ == '__main__':
    add_sections()
