"""basic functions in python"""

PARAM_1_ = 'foo'
PARAM_2_ = 'bar'

#make sure to use 4 whitespaces for scope!
def my_function_name_goes_here(param_1, param_2):
    """prints two parameters on separate lines"""
    print(param_1)
    print(param_2)

#the call
print('1. typical function')
my_function_name_goes_here(PARAM_1_, PARAM_2_)
print()

#optional parameters always at the end of call definition
def my_optional_param_func(mandatory_param, opt_param='default_option_'):
    """function with optional parameters"""
    print(mandatory_param)
    print(opt_param)

#calling with both
print('2. with optional parameter')
my_optional_param_func('foo', 'bar')
#or with mandatory parameter only!
my_optional_param_func('foo')
print()

#function with arbitrary (any!) number of args
def func_with_arbitrary_num_of_args(*args):
    """args are sequence of arbitrary number of arguments"""
    for arg in args:
        print(arg)

#call
print('3. with arbitrary number of args')
MY_ARGS_LIST_ = ['abc', 'arg2', 'moar', 3]
func_with_arbitrary_num_of_args(*MY_ARGS_LIST_) #unpacking list
func_with_arbitrary_num_of_args('abc', 'arg2', 'moar', 3) #literal comma seq
print()

#function with key-word arguments (dict)
print('4. with key-value pairs (kwargs)')
def func_with_kwargs(**kwargs):
    """example function for kwargs (dict param)"""
    for key, value in kwargs.items():
        print(key, ': ', value) #key: value format

#da call
func_with_kwargs(key1='value1', key2='value2')
print()
