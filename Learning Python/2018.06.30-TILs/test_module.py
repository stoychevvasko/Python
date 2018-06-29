'''Unit tests for module.py'''

import pytest
import module as m

def test_method():
    '''Tests module.method().'''

    with pytest.raises(Exception):
        m.method()
