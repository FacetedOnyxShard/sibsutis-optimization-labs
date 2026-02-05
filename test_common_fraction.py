import pytest
from common_fraction import CommonFraction
from common_fraction import Sign


@pytest.fixture
def cf():
    return CommonFraction()


def test_setup_cf(cf):
    cf.top = 10
    cf.bottom = 3

    assert cf.top == 10 and cf.bottom == 3


@pytest.mark.parametrize(
    "a,b,expected",
    [
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
    ],
)
def test_gcd(a, b, expected, cf):
    assert cf.gcd(a, b) == expected
    assert cf.gcd(b, a) == expected


@pytest.mark.parametrize(
    "top, bottom, top_exp, bottom_exp",
    [
        # basic
        (1, 1, 1, 1),
        (2, 2, 1, 1),
        # negative
    ],
)
def test_reduce(top, bottom, top_exp, bottom_exp, cf):
    cf.top = top
    cf.bottom = bottom
    cf.reduce()

    assert cf.top == top_exp and cf.bottom == bottom_exp


@pytest.mark.parametrize(
    "top, bottom, sign, exp_sign",
    [
        pytest.param(5, 5, Sign.PLUS, Sign.PLUS),
        pytest.param(5, -5, Sign.PLUS, Sign.MINUS),
        pytest.param(-5, 5, Sign.PLUS, Sign.MINUS),
        pytest.param(-5, 5, Sign.MINUS, Sign.PLUS),
        pytest.param(5, -5, Sign.MINUS, Sign.PLUS),
        pytest.param(-5, -5, Sign.PLUS, Sign.PLUS),
        pytest.param(-5, -5, Sign.MINUS, Sign.MINUS),
    ],
)
def test_cf_on_init(top, bottom, sign, exp_sign):
    cf = CommonFraction(top, bottom, sign)
    assert cf.sign == exp_sign


@pytest.mark.parametrize(
    "top, bottom, sign, exp_sign",
    [
        pytest.param(5, 5, Sign.PLUS, Sign.PLUS),
        pytest.param(5, -5, Sign.PLUS, Sign.MINUS),
        pytest.param(-5, 5, Sign.PLUS, Sign.MINUS),
        pytest.param(-5, 5, Sign.MINUS, Sign.PLUS),
        pytest.param(5, -5, Sign.MINUS, Sign.PLUS),
        pytest.param(-5, -5, Sign.PLUS, Sign.PLUS),
        pytest.param(-5, -5, Sign.MINUS, Sign.MINUS),
    ],
)
def test_cf_on_set(top, bottom, sign, exp_sign, cf):
    cf.top = top
    cf.bottom = bottom
    cf.sign = sign

    assert cf.sign == exp_sign
