import pytest
from hexlet_pytest.stack import Stack

def test_stack():
    stack = Stack()
    stack.push("one")
    stack.push("two")

    assert stack.pop() == "two"
    assert stack.pop() == "one"

def test_emptiness():
    stack = Stack()
    assert stack.is_empty()
    
    stack.push("one")
    assert not stack.is_empty()
    
    stack.pop()
    assert stack.is_empty()

def test_pop_with_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
