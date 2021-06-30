import pytest
import question2



#test if last word returns length

def word_length(a):
    legth = question2.word_length(a)
    return legth
    

def test_word_legth():
    assert word_length("Django is a good dogy") == 4


#test of string is empty
def empty_string(a):
    empty_string = question2.empty_string(a)
    return empty_string
    
def test_empty_string():
    assert  empty_string("") == 0


#test of string is not empty
def string_is_not_empty(a):
    empty_string = question2.empty_string(a)
    return empty_string
    
def test_string_is_not_empty():
    assert  string_is_not_empty("test") == "string is not empty"

