from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent("Al")
    
def test_noDigit():
    assert findstring.noDigit("n7")