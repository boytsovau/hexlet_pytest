import pytest

def reverse(string):
    return string[::-1]




def test_pop_with_empty_stack():
    stack = [1,2,4]
    with pytest.raises(IndexError):
        stack.pop()

test_pop_with_empty_stack()