import dfa
import time
import pytest
from fixtures import prod_user

def test_empty_class():
    with pytest.raises(TypeError):
        dfa.DFA()

def test_prod_user_token(prod_user):
    assert prod_user.access_token