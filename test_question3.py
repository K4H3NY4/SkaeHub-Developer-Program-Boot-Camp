import pytest
import question3

#check if string is being joined
def is_string_being_joined(x):
    password = question3.listToString(x)
    return password

def test_is_string_bein_joined():
    assert is_string_being_joined(['1','2','3']) == '123'

#test if invalid test will be passed
def is_set_has_main_values(x):
    password = question3.main('w')
    return password

def test_is_set_have_main_values():
    assert is_set_has_main_values('1') == 'invalid text'


#test if string is being randomized
def is_list_being_randomized(m):
    password = question3.randomize(m)
    return password

def test_list_being_randomized():
    assert is_list_being_randomized(['1','e','t']) != '1et'