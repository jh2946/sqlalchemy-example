from app.models import db, Person
import re
from datetime import datetime

while True:

    command = input('Person table action (read/write/exit): ')

    if command == 'read':
        person_list = Person.query.all()
        for person in person_list:
            print()
            print(f'Name: {person.name}')
            print(f'Email: {person.email}')
            if person.bio:
                print(f'Bio: {person.bio}')
            print(f'Age: {person.age}')
            print(f'Balance: {person.balance:.2f}')
            if person.vip:
                print('Is currently a VIP')
            else:
                print('Currently isn\'t a VIP')
            print(f'Sign-up date: {person.signUpDate.date()}')
        print()

    if command == 'write':
        inp_name = input('Name of new person: ')
        while not inp_name or len(inp_name) > 70:
            print('Enter a name with 70 characters or less')
            inp_name = input('Name of new person: ')
        inp_email = input('Email of new person: ')
        while not inp_email or len(inp_email) > 320:
            print('Enter an email with 320 characters or less')
        inp_bio = input('Bio: ')
        inp_age = input('Age: ')
        while not inp_age.isnumeric() or int(inp_age) < 0 or int(inp_age) > 150:
            print('Enter a whole number between 0 and 150 inclusive')
            inp_age = input('Age: ')
        inp_age = int(inp_age)
        inp_balance = input('Balance: ')
        result = re.search('(([1-9][0-9]*)|0)(.[0-9][0-9])?', inp_balance)
        while not result or result.string != inp_balance:
            print('Enter balance as correctly formatted in dollars')
            inp_balance = input('Balance: ')
            result = re.search('(([1-9][0-9]*)|0)(.[0-9][0-9])?', inp_balance)
        inp_balance = float(inp_balance)
        inp_vip = input('Is person a VIP? (y/n): ')
        while inp_vip not in ['y', 'n']:
            print('Please enter either y/n')
            inp_vip = input('Is person a VIP? (y/n): ')
        inp_vip = inp_vip == 'y'
        while True:
            try:
                str_inp_date = input('Enter date joined in YYYY-MM-DD format: ')
                split_inp_date = list(map(int, str_inp_date.split('-')))
                if len(split_inp_date) != 3:
                    raise Exception()
                inp_date = datetime(*split_inp_date)
            except:
                print('Enter date in YYYY-MM-DD format')
                continue
            break
        if inp_bio:
            new_person = Person(
                name=inp_name, 
                email=inp_email,
                bio=inp_bio,
                balance=inp_balance,
                age=inp_age,
                vip=inp_vip,
                signUpDate=inp_date
            )
        else:
            new_person = Person(
                name=inp_name, 
                email=inp_email,
                balance=inp_balance,
                age=inp_age,
                vip=inp_vip,
                signUpDate=inp_date
            )
        db.session.add(new_person)
        db.session.commit()
        print('Person saved into database!')

    if command == 'exit':
        break
