"""Assertions in Python"""

#bool
assert True is True
assert True is not False

#int
assert 1 == True
assert 0 == False

#float
assert 1.0 == True
assert 0.0 == False

#list
assert [] is not True
assert [1] is not False

#tuple
assert () is not True
assert (1) is not False

#str
assert '' is not True
assert 'abc' is not False

#set
assert set() is not True #cause {} is empty dict
assert {'abc'} is not False

#frozenset
assert frozenset() is not True
assert frozenset('abc') is not False

#dict
assert dict() is not True
assert {} is not True #came before set
assert {'key': 'value'} is not False

print('(end of file)')
