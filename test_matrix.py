from fraction import Fraction
from matrix import *


def test_first_step():
    original_matrix = [
        [Fraction(3), Fraction(2), Fraction(5), Fraction(4), Fraction(3)],
        [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-4), Fraction(-2)],
        [Fraction(4), Fraction(1), Fraction(4), Fraction(0), Fraction(2)],
    ]

    a = matrix_copy(original_matrix)

    row = 0
    col = find_enabling_element(a, row)
    a_hat = transform_matrix(a, row, col)
    calculate_elements(a, a_hat, row, col)
    a = matrix_copy(a_hat)

    expected_matrix_after_first_transform = [
        [Fraction(1), Fraction(2, 3), Fraction(5, 3), Fraction(4, 3), Fraction(1)],
        [Fraction(0), Fraction(-5, 3), Fraction(-8, 3), Fraction(-16, 3), Fraction(-3)],
        [Fraction(0), Fraction(-5, 3), Fraction(-8, 3), Fraction(-16, 3), Fraction(-2)],
    ]

    assert FractionMatrixEqual(a, expected_matrix_after_first_transform) == True


def test_strike_rows():
    # 1 0 2 -8 3 -2
    # 0 1 -12 2 2 3
    # 0 0 0 0 0 0
    # 0 0 0 3 0 -1
    # 0 0 0 0 0 0
    original_matrix = read_matrix_from_file("./test_matrix/zero_rows.txt")

    # 1 0 2 -8 3 -2
    # 0 1 -12 2 2 3
    # 0 0 0 3 0 -1
    expected_matrix = [
        [
            Fraction(1),
            Fraction(0),
            Fraction(2),
            Fraction(-8),
            Fraction(3),
            Fraction(-2),
        ],
        [
            Fraction(0),
            Fraction(1),
            Fraction(-12),
            Fraction(2),
            Fraction(2),
            Fraction(3),
        ],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(3), Fraction(0), Fraction(-1)],
    ]

    # вычеркивание работает после подсчета 2 строки
    row = 1  # индекс второй строки 1
    a = matrix_copy(original_matrix)
    a = strike_zero_rows(a, row)

    assert FractionMatrixEqual(a, expected_matrix) == True


def test_matrix_transformation():
    original_matrix = read_matrix_from_file("./test_matrix/pr04_task.txt")

    #  1  -1/2   0    0  -1/2  | -1/2
    #  0    0    1    0     4  |  3
    #  0    0    0    1     0  |  0
    expected_matrix = [
        [
            Fraction(1),
            Fraction(-1, 2),
            Fraction(0),
            Fraction(0),
            Fraction(-1, 2),
            Fraction(-1, 2),
        ],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(4), Fraction(3)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
    ]

    res = Gauss_Jordan_elimination(original_matrix)

    assert FractionMatrixEqual(res, expected_matrix) == True
