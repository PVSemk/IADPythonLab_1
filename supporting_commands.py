import os
import datetime


# Several helpful commands to work with phone book
# Function for clearing the terminal
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# The visualisation of available main commands
def command_visualisation(command_list):
    print('The command list: ')
    for key, values in command_list.items():
        print(key, ' - ', values)

# The visualisation of the certain person
def person_visualisation(phone_book, key):
    # Check if the date exists
    if len(phone_book[key]) == 2:
        print(key, phone_book[key][0], phone_book[key][1], sep=':')
    else:
        print(key, phone_book[key][0], sep=':')

# Checking if the key (Name Surname) is correct
def check_name_surname(id):
    splitted_id = id.split()
    if len(splitted_id) != 2:
        print('Name and Surname input mistake!')
        print('You should write two words divided with whitespace! (Name Surname)')
        return False
    elif not (splitted_id[0].isalnum() and splitted_id[1].isalnum()):
        print('Name and Surname input mistake!')
        print('Name and Surname may contain only letters and numbers! (Name Surname)')
        return False
    elif not (splitted_id[0][0].isalpha() and splitted_id[1][0].isalpha()):
        print('Name and Surname input mistake!')
        print('The first symbols of Name and Surname should be letters!')
        return False
    else:
        return True


# Work with phone number
# Replace +7 with 8
def number_format(number):
    if number[0] == '+' and number[1] == '7':
        return number.replace('+7', '8', 1)
    else:
        return number

# Checking if the phone number is correct
def check_number(number):
    # Check if the number is correct
    if len(number) != 11:
        print('Number input mistake')
        print('You should write 11 digits!')
        return False
    # Check if the first digit is 8
    elif number[0] != '8':
        print('Number input mistake')
        print('Number should begin with +7 or 8')
        return False
    # Check if there is not a digit in the number
    elif not all(letter.isdigit() for letter in number):
        print('Number input mistake')
        print('You should write only digits')
        return False
    else:
        return True


# Check if the date of birthday is correct
def check_bd_date(date):
    today = datetime.date.today()
    try:
        check_date = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    except ValueError:
        print('Date of birthday input mistake')
        print('Required format: XX/XX/XXXX(if year is asked)')
        print('Please, check if you entered correct day, month and year')
        return False
    if check_date > today:
        print ('Date of birthday input mistake')
        print ('Your person will be born in the Future. Please, check the year')
        return False
    return True

# Checking if the value (Number, Date of birthday) is correct and make it correct (if possible)
def check_value(value):
    # Check if the value has an appropriate size and contains no empty fields
    if len(value) == 1 and value[0] != '':
        # Check if the number begins with +7 and replace it with 8
        value[0] = number_format(value[0])
        return check_number(value[0])
    elif len(value) == 2 and value[0] != '' and value[1] != '':
        value[0] = number_format(value[0])
        return check_number(value[0]) and check_bd_date(value[1])
    else:
        print('Value input mistake!')
        print('You should write one or two not-empty fields (Number, Date of birthday (optional)')
        return False

# Checking if the choice (e.g choice of the option for searching) was made right
def check_choice(min, max, choice):
    try:
        if min <= int(choice) <= max - 1:
            return 1
        # Signal if the user decided to return into the main menu of the phone book
        elif int(choice) == max:
            return 0
        # Incorrect input, digit out of range
        else:
            return -1
    # Incorrect input, the symbol is not a digit
    except ValueError:
        return -1

