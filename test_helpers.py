from matrix import is_identity_matrix
from fraction import Fraction


def test_identity_func_correct():
    identity_matrix = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(10)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(30)],
    ]
    assert is_identity_matrix(identity_matrix) == True


def test_identity_func_incorrect():
    not_identity_matrix = [
        [Fraction(0), Fraction(1), Fraction(0), Fraction(10)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(30)],
    ]
    assert is_identity_matrix(not_identity_matrix) == False


def test_identity_func_incorrect_for_task():
    not_identity_matrix = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(10)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(20)],
    ]
    assert is_identity_matrix(not_identity_matrix) == False
