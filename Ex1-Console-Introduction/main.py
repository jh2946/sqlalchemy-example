from app.models import Person, db

while True:

    command = input('Person table action (read/write/exit): ')

    if command == 'write':
        inp_name = input('Name of new person: ')
        inp_email = input('Email of new person: ')
        new_person = Person(
            name=inp_name,
            email=inp_email
        )
        db.session.add(new_person)
        db.session.commit()
        print('Person saved into database!')

    if command == 'read':
        person_list = Person.query.all()
        for person in person_list:
            print()
            print(f'Name: {person.name}')
            print(f'Email: {person.email}')
        print()

    if command == 'exit':
        break
