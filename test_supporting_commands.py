import supporting_commands as func
# This file contains only testing for functions which are in supporting_commands.py
# In the file commands.py there is a number of functions which contain required input checking
# Which is not in supporting_commands.py (functions delete_person_by_number or search)
# However, principle is the same
# So I decided not to rewrite these segments
def test_check_value():
    # If no birthday was entered, the list contains only number
    # Due to transformations made in the main module
    # That is why test ['Correct number', ''] is False
    assert func.check_value(['']) == 0
    assert func.check_value(['sadass']) == 0
    assert func.check_value(['', 'asdsaad']) == 0
    assert func.check_value(['+78005553535']) == 1
    assert func.check_value(['+78005553535', '']) == 0
    assert func.check_value(['+78005553535', ' ']) == 0
    assert func.check_value(['88005553535']) == 1
    assert func.check_value(['98006665656']) == 0
    assert func.check_value(['890055565656']) == 0
    assert func.check_value(['88005553535', 'asd']) == 0
    assert func.check_value(['', '12/12/1989']) == 0
    assert func.check_value(['8+7910345435', '12/12/1989']) == 0
    assert func.check_value(['89103943410', '30/12/2045']) == 0
    assert func.check_value(['+78005553535', '30/11/2018']) == 1


def test_check_bd_date():
    assert func.check_bd_date('22/11/1986') == 1
    assert func.check_bd_date('100/11/1986') == 0
    assert func.check_bd_date('0/11/1986') == 0
    assert func.check_bd_date('22/0/1986') == 0
    assert func.check_bd_date('28/1/-100') == 0
    assert func.check_bd_date('31/12/1486') == 1
    assert func.check_bd_date('sdfdsfsdfsd') == 0
    assert func.check_bd_date('sdf/dsfs/dfsd') == 0
    assert func.check_bd_date('') == 0
    assert func.check_bd_date('1233452345') == 0
    assert func.check_bd_date('12/123') == 0
    assert func.check_bd_date('ываыва') == 0
    assert func.check_bd_date('0/0/0') == 0
    assert func.check_bd_date('31/12/2018') == 0
    assert func.check_bd_date('29/11/2045') == 0


def test_check_name_surname():
    assert func.check_name_surname('Pavel Semkin') == 1
    assert func.check_name_surname('pavel semkin') == 1
    assert func.check_name_surname('Petr') == 0
    assert func.check_name_surname('Sasd.sdfsdf sdf.sdf.sdfsdf') == 0
    assert func.check_name_surname('123324646463452 12341321234') == 0
    assert func.check_name_surname('_____ asdfasdfsdf _____') == 0
    assert func.check_name_surname('____ _____') == 0
    assert func.check_name_surname('Sasha1 Petrov') == 1
    assert func.check_name_surname('1asha1 2etrov') == 0
    assert func.check_name_surname('1asha1 petrov') == 0
    assert func.check_name_surname('\n') == 0


def test_check_number():
    assert func.check_number('89101418456') == 1
    assert func.check_number('8910141845') == 0
    assert func.check_number(func.number_format('+79101418456')) == 1
    assert func.check_number(func.number_format('+79101418456123123')) == 0
    assert func.check_number('Wrong input') == 0
    assert func.check_number('89101sdffsdf') == 0
    assert func.check_number('8+7+7+7+7+7+7+7+7+7+7') == 0
    assert func.check_number('8910 123123 123123') == 0
    assert func.check_number('99101412356') == 0
    assert func.check_number('8910141845+7') == 0
    assert func.check_number('891014184+7') == 0
    assert func.check_number('\n') == 0


def test_check_choice():
    assert func.check_choice(1, 6, '123') == -1
    assert func.check_choice(1, 6, '1') == 1
    assert func.check_choice(1, 6, '3') == 1
    assert func.check_choice(1, 6, '6') == 0
    assert func.check_choice(1, 6, 'asdasd') == -1
    assert func.check_choice(1, 6, '') == -1
    assert func.check_choice(1, 6, '12.5') == -1
    assert func.check_choice(1, 6, '12/5') == -1
    assert func.check_choice(1, 6, ' ') == -1
    assert func.check_choice(1, 6, '\n') == -1

