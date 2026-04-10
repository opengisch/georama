import pytest

from georama.maps.interfaces.georama.requests import handle_list_encoding


@pytest.mark.parametrize(
    "parameter_value,expected", [("a,b,c", ["a,b,c"]), ("(a,b,c)(d,e,f)", ["a,b,c", "d,e,f"])]
)
def test_handle_list_encoding(parameter_value, expected):
    assert handle_list_encoding(parameter_value) == expected
