"""insert docstring text here, triple quotes all the way"""
HELLO_WORLD_ = 'Hello, world!'
print(HELLO_WORLD_) #same-line comment
#standard new-line comment - Python's interpreter will ignore it

HELLO_WORLD_LIST_ = list(HELLO_WORLD_) #constructs list from str
print(" * As list: ")
print(HELLO_WORLD_LIST_)

HELLO_WORLD_SET_ = set(HELLO_WORLD_) #constructs set from str
print(' * As set:')
print(HELLO_WORLD_SET_)

HELLO_WORLD_FROZENSET_ = frozenset(HELLO_WORLD_LIST_) #constructs frozenset from str
print(' * As frozenset:')
print(HELLO_WORLD_FROZENSET_)

USER_INPUT_ = input('echo: ') #reads keyboard input
print(' * echo-back: ' + USER_INPUT_) #echoes it back

print("'Double quotes or single, it's OK'") #TIL
print('"Or the other way around"') #moar?
