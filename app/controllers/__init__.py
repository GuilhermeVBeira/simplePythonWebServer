from app.models.tables import Person
import json

def save_person(db, person):
	template = 'index.html'
	print(person)
	pessoa = Person(firstname=person['firstname'][0], lastname=person['lastname'][0], adress=person['adress'][0])
	db.add(pessoa)
	db.commit()
	# print(kwargs)
	return template

def delete_person(db, person):
	template = 'index.html'
	try:
		person = db.query(Person).filter(Person.id == person['id'][0]).one()
		db.delete(person)
		db.commit()
	except expression as identifier:
		pass
	return template

def index():
    template = 'index.html'
    return template

def get_persons(db):
	pessoas = db.query(Person).all()
	columns = Person.__table__.columns
	campos= [str(colum).split('.')[1] for colum in columns]
	list_pessoas = []	
	for pessoa in pessoas:
		d = {}
		for campo in campos:
			d[campo]= pessoa.__dict__[campo]
		list_pessoas.append(d)
	return json.dumps(list_pessoas) 

def get_person(db, person):
	person = db.query(Person).filter(Person.id == person['id'][0]).one()
	columns = Person.__table__.columns
	campos= [str(colum).split('.')[1] for colum in columns]
	d ={}
	for campo in campos:
		d[campo]= person.__dict__[campo]
	return json.dumps(d) 

def edit_person(db, person):
	
	persontoUpDate = db.query(Person).filter(Person.id == person['id'][0]).one()
	persontoUpDate.firstname = person['firstname'][0]
	persontoUpDate.lastname = person['lastname'][0]
	persontoUpDate.adress = person['adress'][0]
	db.commit()
	d ={}
	return json.dumps(d) 