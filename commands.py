import supporting_commands


# Main commands of the phone book
# Add a person into the phone book
def add_person(phone_book, *person):
    if person[0] in phone_book:
        print('Your person is already in the phone book')
        print('Choose an option:')
        print('1. Update the fields')
        print('2. Change name and surname of the new person')
        print('3. Return to the main menu')
        choice = input('Enter your number: ')
        if choice == '1':
            # Check if there is date of birthday in new data and in data-to-be-updated
            # The first statement checks if in our data-to-be-updated there are both a number and a date of birthday
            # The second statement checks if in "person" there is only a name and a number
            if len(phone_book[person[0]]) == 2 and len(person[1]) == 1:
                # Replace the number and do not touch the date
                phone_book[person[0]][0] = person[1][0]
            else:
                # In other cases just replace all data
                phone_book[person[0]] = person[1]
            print('Person was successfully added!')
            input('\nPress Enter to return into main menu')
            supporting_commands.cls()

        elif choice == '2':
            supporting_commands.cls()
            print('Enter new name and surname')
            print('Example: Pavel Semkin')
            new_person = input("Enter here: ").title()
            new_person = ' '.join(new_person.split())
            if supporting_commands.check_name_surname(new_person):
                # If the new data is already in the phone book again
                if new_person in phone_book:
                    supporting_commands.cls()
                    print('Sorry, but you should write data which is not in your phone book')
                    print('Try again!')
                    add_person(phone_book, new_person, person[1])
                else:
                    phone_book[new_person] = person[1]
                    print('Person was successfully added!')
                    input('\nPress Enter to return into main menu')
                    supporting_commands.cls()

            else:
                print('Please, write appropriate data next time')
                input('Press Enter to return into the main menu')
                supporting_commands.cls()

        elif choice == '3':
            supporting_commands.cls()

        else:
            supporting_commands.cls()
            print('Incorrect option')
            print('Please, choose an appropriate option next time')
            input('\nPress Enter to return into main menu')
    # Person is not in the phone book
    # Just add a new field
    else:
        phone_book[person[0]] = person[1]
        print('Person was successfully added!')
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()


# The visualisation of the whole phone book
def visualisation(phone_book):
        supporting_commands.cls()
        print("This is all your phone book")
        print("Output format is Name Surname:Number:Date of birth(if exists)")
        print("Date of birth format: XX/XX/XXXX\n")
        for key in phone_book.keys():
            supporting_commands.person_visualisation(phone_book, key)
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()


# Searching in phone book
def search(phone_book, choice):
    supporting_commands.cls()
    no_match = 0
    # Algorithms for name-only and surname-only are almost equal
    # I decided to combine them into one "if"
    if choice == '1' or choice == '2':
        if choice == '1':
            print('Searching by name')
        else:
            print('Searching by surname')
        # Remove leading and tailing whitespaces and capitalize the first letter
        search_object = input('Enter data (Full name or Surname): ').title().strip()
        # Check if search object is correct
        # This part of code is used only once (although it is almost identical to check_name_and_surname function)
        # So I decided not to create a function for it
        if len(search_object.split()) != 1:
            print('Name or Surname input mistake!')
            print('You should write one word')
        elif not search_object.isalnum():
            print('Name or Surname input mistake!')
            print('This field may contain only letters and numbers')
        elif not search_object[0].isalpha():
            print('Name or Surname input mistake!')
            print('The first symbol should be a letter')
        else:
            print("\nSearching results:")
            for key in phone_book.keys():
                # Decide if we search by name or by surname
                if (choice == '1' and search_object == key.split()[0]) or (choice == '2' and search_object == key.split()[1]):
                    supporting_commands.person_visualisation(phone_book, key)
                else:
                    # Counting a number of positions that are not appropriate
                    no_match += 1
            if no_match == len(phone_book):
                print("No matches were found")
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()

    elif choice == '3':
        print('Searching by name and surname')
        search_object = input('Enter your data: ').title()
        search_object = ' '.join(search_object.split())
        if supporting_commands.check_name_surname(search_object):
            print("\nSearching results:")
            for key in phone_book.keys():
                if search_object == key:
                    supporting_commands.person_visualisation(phone_book, key)
                else:
                    no_match += 1
            if no_match == len(phone_book):
                print("No matches were found")
        else:
            print('Please, write appropriate data next time')
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()


    elif choice == '4':
        print('Searching by phone number')
        search_object = input('Enter your data: ')
        if supporting_commands.check_number(search_object):
            print("\nSearching results:")
            for key, value in phone_book.items():
                if search_object == value[0]:
                    supporting_commands.person_visualisation(phone_book, key)
                else:
                    no_match += 1
            if no_match == len(phone_book):
                print('No matches were found')
        else:
            print('Please, write appropriate data next time')
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()

    elif choice == '5':
        print('Searching by date of birthday')
        print('Data format: XX/XX/XXXX')
        search_object = input('Enter your data: ')
        if supporting_commands.check_bd_date(search_object):
            # Convert object into date format
            search_object = supporting_commands.datetime.datetime.strptime(search_object, '%d/%m/%Y').date()
            print("\nSearching results:")
            for key, value in phone_book.items():
                if len(value) == 2:
                    date_value = supporting_commands.datetime.datetime.strptime(value[1], '%d/%m/%Y').date()
                    if search_object == date_value:
                        supporting_commands.person_visualisation(phone_book, key)
                    else:
                        no_match += 1
                else:
                    no_match += 1
            if no_match == len(phone_book):
                print('No matches were found')
        else:
            print('Please, write appropriate data next time')
        input('\nPress Enter to return into main menu')
        supporting_commands.cls()


# Find age of a person
def get_age(phone_book, key):
    if key not in phone_book:
        print('Sorry, you don\'t have this person in your phone book')
        return -1

    elif len(phone_book[key]) == 1:
        print('This person has no assigned date of birthday')
        return -1

    else:
        today = supporting_commands.datetime.date.today()
        # Split the date of birthday into three strings
        split_date = phone_book[key][1].split('/')
        born_year = int(split_date[2])
        born_month = int(split_date[1])
        born_day = int(split_date[0])
        # Count the age of the person
        age = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
        return age


# Change any data in the phone book
def change_data(phone_book, choice):
    supporting_commands.cls()
    print('Please, enter name and surname of a person whose data you want to change')
    print('Example: Pavel Semkin')
    key = input('Enter here: ').title()
    key = ' '.join(key.split())
    if supporting_commands.check_name_surname(key):
        if key not in phone_book:
            print('Sorry, you don\'t have this person in your phone book')
            input('\nPress Enter to return into main menu')
            supporting_commands.cls()
        else:
            if choice == '1':
                print('\nPlease, enter new name and surname')
                print('Example: Pavel Semkin')
                new_data = input('Enter here: ').title()
                new_data = ' '.join(new_data.split())
                if supporting_commands.check_name_surname(new_data):
                    if new_data == key:
                        print('It is the same person')
                        input('Press Enter to return into main menu')
                        supporting_commands.cls()
                    elif new_data in phone_book:
                        print('\nYou already have this person in your phone book')
                        print('Do you want to replace his data?')
                        print('WARNING! You will lose the old data')
                        print('Enter your choice (Y/N):', end=' ')
                        confirm = input()
                        if confirm == 'Y':
                            phone_book[new_data] = phone_book.pop(key)
                            print('Success!')
                            input('\nPress Enter to return into main menu')
                            supporting_commands.cls()
                        elif confirm == 'N':
                            input('\nPress Enter to return into main menu')
                            supporting_commands.cls()
                        else:
                            supporting_commands.cls()
                            print('Please, choose an appropriate option next time')
                            input('Press Enter to return into main menu')
                            supporting_commands.cls()
                    else:
                        phone_book[new_data] = phone_book.pop(key)
                        print('Success!')
                        input('\nPress Enter to return into main menu')
                        supporting_commands.cls()

            elif choice == '2':
                print('\nPlease, enter new phone number')
                print('Example: 88005553535')
                new_number = input('Enter number here: ')
                # Replace +7 with 8 and check if numer is correct
                new_number = supporting_commands.number_format(new_number)
                if supporting_commands.check_number(new_number):
                    phone_book[key][0] = new_number
                    print('Success!')
                input('\nPress Enter to return into main menu')
                supporting_commands.cls()

            elif choice == '3':
                print('\nPlease, enter new date of birthday')
                print('Format: XX/XX/XXXX')
                new_date = input('Enter here: ')
                # Check if date is correct
                if supporting_commands.check_bd_date(new_date):
                    # Check if the person didn't have "date of birthday" field
                    if len(phone_book[key]) == 1:
                        phone_book[key].append(new_date)
                    else:
                        phone_book[key][1] = new_date
                    print('Success!')
                input('\nPress Enter to return into main menu')
                supporting_commands.cls()
    else:
        print('Please, write appropriate data next time')
        input('Press Enter to return into the main menu')
        supporting_commands.cls()


# Delete a person from the phone book by name
def delete_person_by_name(phone_book, name):
    if name in phone_book:
       del phone_book[name]
       print('{} was deleted from your phone book'.format(name))
    else:
        print('Sorry, but you don\'t have this person in your phone book')


# Delete a person/persons from the phone book by number
def delete_person_by_number(phone_book, number):
    supporting_commands.cls()
    index = 1
    # Create a dict which contains people who will probably be deleted
    people_to_delete = {}
    print('These people have the number which was entered:')
    for key, value in phone_book.items():
        if value[0] == number:
            print('{}.'.format(index), end=' ')
            supporting_commands.person_visualisation(phone_book, key)
            people_to_delete[index] = key
            index += 1
    # Noone was found
    if people_to_delete == {}:
        print('No people were found')

    # Only one person was found
    elif len(people_to_delete) == 1:
        # Delete this person
        delete_person_by_name(phone_book, people_to_delete[1])
    # Several persons were found
    # Ask the user what to do
    else:
        print('Please, choose the options which you want to delete')
        print('If you want to delete several people, please enter options as in example')
        print('Example: Option1 Option2 Option3')
        choices = input('Enter here: ')
        choices = choices.split()
        for choice in choices:
            # Try to catch input mistakes
            # I decided not to push this block into a function
            # That means in cannot be tested with py.test
            try:
                choice = int(choice)
                if people_to_delete[choice] in phone_book:
                    delete_person_by_name(phone_book, people_to_delete[choice])
                else:
                    print('You have already deleted {}'.format(people_to_delete[choice]))
            except ValueError:
                print('Input error!', end=' ')
                print('You should write only digits divided by whitespaces')
            except KeyError:
                print('Input error!', end=' ')
                print('You should choose digits which are offered')


# Find people who are younger/equal/older than entered age
def sort_by_age(phone_book, age_to_sort):
    supporting_commands.cls()
    # Check if entered age is correct
    try:
        age_to_sort = int(age_to_sort)
    except ValueError:
        print('Input mistake!')
        print('Please, enter one number next time')
        input('Press Enter to return into main menu')
    else:
        if age_to_sort <= 0:
            print('Input mistake!')
            print('Please, enter an appropriate age next time')
            input('Press Enter to return into main menu')
        else:
            # Generate a list with tuples (Person, Age)
            persons_age = [(key, get_age(phone_book, key)) for key in phone_book if len(phone_book[key]) == 2]
            # Sort this list by value
            persons_age.sort(key=lambda tup: tup[1])
            # Iterate over the created list and visualise appropriate people
            # Flag-variables indicate that we have visualised one of possible groups of people
            flag_equal = True
            flag_older = True
            flag_younger = True
            for pair in persons_age:
                if pair[1] < age_to_sort and flag_younger:
                    flag_younger = False
                    print('People who are younger than {}:'.format(age_to_sort))

                if flag_equal and pair[1] == age_to_sort:
                    flag_equal = False
                    print('\nPeople whose age is equal to {}:'.format(age_to_sort))

                if flag_older and pair[1] > age_to_sort:
                    flag_older = False
                    print('\nPeople who are older than {}'.format(age_to_sort))

                supporting_commands.person_visualisation(phone_book, pair[0])
            input('\nPress Enter to return into main menu')


# Find people whose birthday comes during a month
def search_by_bd(phone_book, date):
    date = supporting_commands.datetime.datetime.strptime(date + '/2004', '%d/%m/%Y').date()
    match = 0
    print('Results: ')
    for key, value in phone_book.items():
        if len(value) == 2:
            # Converts value into date object
            check_date = supporting_commands.datetime.datetime.strptime(value[1][:-5] + '/2004', '%d/%m/%Y').date()
            if check_date == date:
                supporting_commands.person_visualisation(phone_book, key)
                match += 1
    if match == 0:
        print('No one was found')



