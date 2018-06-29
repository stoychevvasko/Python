'''Sub-module tests.'''

import pytest
# 1. # from module_dir import sub_module
# 2. # from module_dir.sub_module import sub_method
import module_dir.sub_module as sm

def test_sub_method():
    '''Tests sub method.'''
    with pytest.raises(TypeError):
        # 1. # sub_module.sub_method()
        # 2. # sub_method()
        sm.sub_method()
