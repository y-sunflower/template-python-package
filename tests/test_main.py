import pytest
from package_name import add_digit


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (10, 1, 11),
        (10, 10, 20),
        (15, 0, 15),
    ],
)
def test_sum_digit(a, b, expected):
    assert add_digit(a, b) == expected
