import commands


def main():
    # Declaration block
    COMMAND_LIST = {
        '1. Stop': "If you want to stop using our phone book, you should use this command",
        '2. Add persons': "You can add persons to Phone book",
        '3. Visualisation': "You can see all elements of Phone book",
        '4. Search': 'Searching over phone book by one or several fields',
        '5. Get the age of the person': "You can get the current age of the person",
        '6. Update data': "You can change any field of the person",
        '7. Delete person by number': "You can delete a record by number",
        '8. Delete person by name': 'You can delete a record by name',
        '9. Divide by age': 'Visualise persons who are younger/equal/older than N years',
        '10. Search by date (non-year)': 'Search people by birthday without taking year into account'
        }
    phone_book = {}

    # Iterate every line
    # Every line is checked and added only if it is correct
    # In other cases, error message is outputted
    with open('phone_book.txt', 'r') as file:
        commands.supporting_commands.cls()
        for line in file:
            key, *value = line.replace('\n', ':').split(':')
            # Remove "" element which appeared after replacing \n symbol with :
            if '' in value:
                value.remove('')
            if key in phone_book:
                print('Skipping contact {} with phone number {}'.format(key, value[0]))
                print('He/she has been already loaded with another phone number {}'.format(phone_book[key][0]))
                print('You can change his/her data using "update data" command\n')
                continue
            if commands.supporting_commands.check_name_surname(key):
                # Value contains number, date
                if len(value) == 2:
                    value[0] = commands.supporting_commands.number_format(value[0])
                    if (commands.supporting_commands.check_number(value[0])
                            and commands.supporting_commands.check_bd_date(value[1])):
                        # Capitalize letters
                        phone_book[key.title()] = value
                    else:
                        print('Skipping contact {}\n'.format(key))
                # Value contains only number and "" which contained \n symbol
                elif len(value) == 1:
                    value[0] = commands.supporting_commands.number_format(value[0])
                    if commands.supporting_commands.check_number(value[0]):
                        phone_book[key.title()] = value
                    else:
                        print('Skipping contact {}\n'.format(key))
                # Value contains rubbish
                else:
                    print('Skipping contact {}\n'.format(key))
            else:
                    print('Skipping contact {}\n'.format(key))

    print('\nAll persons were loaded')
    input('Press Enter to launch the main menu')
    # Initial clearing of the terminal
    commands.supporting_commands.cls()
    # While-cycle for the interaction with the phone book
    while True:
        print('Welcome to your phone book!')
        print('Enter the command, please:')
        commands.supporting_commands.command_visualisation(COMMAND_LIST)
        command = input('Input number here: ')
        if command == '1':
            commands.supporting_commands.cls()
            break

        elif command == '2':
            commands.supporting_commands.cls()
            print('Enter your data (Name Surname:Number:Date of birth(optional)')
            print('Date of birth format: XX/XX/XXXX')
            print('Example: Pavel Semkin:88005553535:09/09/1999')
            print('Or enter "q" or "Q" to return into the main menu')
            # Capitalize the first letter of name and surname
            data = input("Enter here: ").title()
            if data == 'Q':
                commands.supporting_commands.cls()
            else:
                commands.supporting_commands.cls()
                key, *value = data.replace('\n', ':').split(':')
                # Remove excessive whitespaces
                key = ' '.join(key.split())
                if (commands.supporting_commands.check_name_surname(key)
                        and commands.supporting_commands.check_value(value)):
                    commands.add_person(phone_book, key, value)
                else:
                    print('Please, write appropriate data next time')
                    input('Press Enter to return into the main menu')
                    commands.supporting_commands.cls()

        elif command == '3':
            commands.supporting_commands.cls()
            commands.visualisation(phone_book)

        elif command == '4':
            commands.supporting_commands.cls()
            print('What fields do you want to use for searching?')
            print('Please, choose ONE option')
            print('1. Name')
            print('2. Surname')
            print('3. Name and Surname')
            print('4. Number')
            print('5. Date of birthday')
            print('6. Return to the main menu')
            choice = input('Enter your number here: ')
            # Check if the choice is appropriate
            if commands.supporting_commands.check_choice(1, 6, choice) == 1:
                commands.search(phone_book, choice)
                # Return to the main menu was checked
            elif commands.supporting_commands.check_choice(1, 6, choice) == 0:
                commands.supporting_commands.cls()
                # Incorrect choice
            else:
                commands.supporting_commands.cls()
                print('Please, choose an appropriate option for searching next time')
                input('Press Enter to return into the main menu')
                commands.supporting_commands.cls()

        elif command == '5':
            commands.supporting_commands.cls()
            print('Enter name and surname of the person')
            print('Example: Pavel Semkin')
            print('Or enter "Q" or "q" to return into the main menu')
            name_and_surname = input('Input here: ').title()
            if name_and_surname == 'Q':
                commands.supporting_commands.cls()
            else:
                name_and_surname = ' '.join(name_and_surname.split())
                if commands.supporting_commands.check_name_surname(name_and_surname):
                    age = commands.get_age(phone_book, name_and_surname)
                    # Check if everything is correct
                    if age != -1:
                        print('The age of your person is {}'.format(age))
                    input('Press Enter to return into main menu')
                    commands.supporting_commands.cls()
                else:
                    print('Please, write appropriate data next time')
                    input('Press Enter to return into the main menu')
                    commands.supporting_commands.cls()

        elif command == '6':
            commands.supporting_commands.cls()
            print('What data do you want to change?')
            print('1. Name and surname')
            print('2. Number')
            print('3. Date of birthday')
            print('4. Return to the main menu')
            choice = input('Enter your number here: ')
            if commands.supporting_commands.check_choice(1, 4, choice) == 1:
                commands.change_data(phone_book, choice)
            elif commands.supporting_commands.check_choice(1, 4, choice) == 0:
                commands.supporting_commands.cls()
            else:
                commands.supporting_commands.cls()
                print('Please, choose an appropriate option for changing next time')
                input('Press Enter to return into the main menu')
                commands.supporting_commands.cls()

        elif command == '7':
            commands.supporting_commands.cls()
            print('Who do you want to delete?')
            print('Enter a number (11 digits)')
            print('Example: 88005553535')
            print('Or enter "Q" or "q" to return into the main menu')
            number = input('Enter here: ').title()
            if number == 'Q':
                commands.supporting_commands.cls()
            else:
                number = commands.supporting_commands.number_format(number)
                if commands.supporting_commands.check_number(number):
                    commands.delete_person_by_number(phone_book, number)
                    input('\nPress Enter to return into main menu')
                    commands.supporting_commands.cls()
                else:
                    input('\nPress Enter to return into main menu')
                    commands.supporting_commands.cls()

        elif command == '8':
            commands.supporting_commands.cls()
            print('Who do you want to delete?')
            print('Input format: Name Surname')
            print('Example: Pavel Semkin')
            print('Or enter "Q" or "q" to return into the main menu')
            name = input('Enter here: ').title()
            if name == 'Q':
                commands.supporting_commands.cls()
            else:
                name = ' '.join(name.split())
                if commands.supporting_commands.check_name_surname(name):
                    commands.delete_person_by_name(phone_book, name)
                    input('\nPress Enter to return into main menu')
                    commands.supporting_commands.cls()
                else:
                    print('Please, write appropriate data next time')
                    input('Press Enter to return into the main menu')
                    commands.supporting_commands.cls()

        elif command == '9':
            commands.supporting_commands.cls()
            print('Enter a number for finding people who are younger/equal/older than your number')
            print('Or enter "q" or "Q" to return into main menu')
            age_to_sort = input('Enter here: ')
            if age_to_sort == 'Q' or age_to_sort == 'q':
                commands.supporting_commands.cls()
            else:
                # All visualisation aspects are inside the function
                commands.sort_by_age(phone_book, age_to_sort)
                commands.supporting_commands.cls()

        elif command == '10':
            commands.supporting_commands.cls()
            print('Searching people by birthday without year')
            print('Please, enter your date')
            print('Format: XX/XX')
            date = input('Enter here: ')
            # Add a year in order to use original check_bd_date function
            if commands.supporting_commands.check_bd_date(date + '/2004'):
                commands.search_by_bd(phone_book, date)
                input('\nPress Enter to return into main menu')
                commands.supporting_commands.cls()
            else:
                print('Please, write appropriate data next time')
                input('Press Enter to return into main menu')
                commands.supporting_commands.cls()

        else:
            commands.supporting_commands.cls()
            print('Please, wright correct number!\n')
    # End of interaction with phone book
    commands.supporting_commands.cls()
    print('Thanks for using the phone book!')
    print('Good Luck!')

    # Save your phone book
    # It is saved into another file in order to show how input works with incorrect data
    with open('phone_book_saved.txt', 'w') as file:
        for key, value in phone_book.items():
            # Check if date of birthday exists
            if len(value) == 2:
                file.write('{}:{}:{}\n'.format(key, value[0], value[1]))
            else:
                file.write('{}:{}\n'.format(key, value[0]))
        print('Your data was saved into phone_book_saved.txt')


if __name__ == "__main__":
    main()
