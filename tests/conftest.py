import pytest
import os
import regex
from random import randbytes


@pytest.fixture
def luac_filenames():
    data_dir = os.path.dirname(__file__) + os.sep + 'data'
    r = regex.compile(r'^v.{3}\.luac64')
    result = []
    for f in os.listdir(data_dir):
        if r.match(f):
            result.append(data_dir + os.sep + f)
    return result


@pytest.fixture
def luac_files(luac_filenames):
    result = []
    for filename in luac_filenames:
        with open(filename, 'rb') as f:
            result.append(f.read())
    return result


@pytest.fixture
def broken_luac():
    return b'Lua\51' + randbytes(1000)