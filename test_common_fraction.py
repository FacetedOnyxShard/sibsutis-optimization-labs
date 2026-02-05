import pytest
from common_fraction import CommonFraction

@pytest.fixture
def cf():
    return CommonFraction()

def test_setup_cf(cf):
    cf.top = 10
    cf.bottom = 3

    assert cf.top == 10 and cf.bottom == 3

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 1),
    (2, 4, 2),
    (12, 8, 4),
    (54, 24, 6),
    (13, 13, 13),
    (0, 10, 10),
    (10, 0, 10),
    (-10, 15, 5),
    (10, -15, 5),
    (-10, -15, 5),
    (1071, 462, 21), 
])
def test_gcd(a, b, expected, cf):
    assert cf.gcd(a,b) == expected
    assert cf.gcd(b,a) == expected


@pytest.mark.parametrize("top, bottom, top_exp, bottom_exp", [
    # basic
    (1, 1, 1, 1),
    (2, 2, 1, 1),

    # negative
])
def test_reduce(top, bottom, top_exp, bottom_exp, cf):
    cf.top = top
    cf.bottom = bottom
    cf.reduce()

    assert cf.top == top_exp and cf.bottom == bottom_exp