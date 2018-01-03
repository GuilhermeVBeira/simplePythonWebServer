import json

from app.models import Person
from app.settings import TEMPLATE_ROOT


def get_home():
    return open(TEMPLATE_ROOT + 'index.html').read()


def get_fields(columns):
    return [str(colum).split('.').pop() for colum in columns]


def save_person(db, data):
    person = Person(firstname=data['firstname'][0], lastname=data['lastname'][0], address=data['address'][0])
    db.add(person)
    db.commit()
    return None


def delete_person(db, data):
    try:
        person = db.query(Person).filter(Person.id == data['id'][0]).one()
        db.delete(person)
        db.commit()
    except expression as identifier:
        pass
    return None


def get_people(db, data):
    people = db.query(Person).all()
    fields = get_fields(Person.__table__.columns)
    list_people = [{field: person.__dict__[field] for field in fields} for person in people]
    return json.dumps(list_people) 


def get_person(db, data):
    person = db.query(Person).filter(Person.id == data['id'][0]).one()
    fields = get_fields(Person.__table__.columns)
    d = {field: person.__dict__[field] for field in fields}
    return json.dumps(d) 


def edit_person(db, data):
    person = db.query(Person).filter(Person.id == data['id'][0]).one()
    person.firstname = data['firstname'][0]
    person.lastname = data['lastname'][0]
    person.address = data['address'][0]
    db.commit()
    return None
