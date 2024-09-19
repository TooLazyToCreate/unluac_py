import pytest
from unluac import decompile_file, decompile


@pytest.mark.usefixtures("luac_filenames")
def test_decompile_file(luac_filenames):
    for f in luac_filenames:
        d = decompile_file(f)
        assert type(d) == str and len(d) > 10


@pytest.mark.usefixtures("luac_files")
def test_decompile(luac_files):
    for f in luac_files:
        d = decompile(f)
        assert type(d) == str and len(d) > 10


def test_empty_data():
    with pytest.raises(Exception) as e_info:
        decompile(b'')


@pytest.mark.usefixtures("broken_luac")
def test_broken_luac(broken_luac):
    with pytest.raises(Exception) as e_info:
        decompile(broken_luac)