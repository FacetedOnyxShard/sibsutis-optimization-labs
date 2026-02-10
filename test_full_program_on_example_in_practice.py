from matrix import *
import pytest


def test_pr01():
    original_matrix = read_matrix_from_file("./test_matrix/pr01_task.txt")
    expected_matrix = read_matrix_from_file("./test_matrix/pr01_answer.txt")
    expected_answer = Answer.No
    expected_system = {}

    eliminated_matrix = Gauss_Jordan_elimination(original_matrix)

    assert matrices_are_equal(eliminated_matrix, expected_matrix)

    answer, system = find_system_solution(eliminated_matrix)

    assert answer == expected_answer and system == expected_system


def test_pr04():
    original_matrix = read_matrix_from_file("./test_matrix/pr04_task.txt")
    expected_matrix = read_matrix_from_file("./test_matrix/pr04_answer.txt")
    expected_answer = Answer.Infinity
    expected_system = {}
    expected_system["x1"] = sympify("-1/2 + 1/2*x2 + 1/2*x5")
    expected_system["x3"] = sympify("3 - 4*x5")
    expected_system["x4"] = sympify("0")

    eliminated_matrix = Gauss_Jordan_elimination(original_matrix)

    assert matrices_are_equal(eliminated_matrix, expected_matrix)

    answer, system = find_system_solution(eliminated_matrix)

    assert answer == expected_answer
    assert system == expected_system


def test_pr05():
    original_matrix = read_matrix_from_file("./test_matrix/pr05_task.txt")
    expected_matrix = read_matrix_from_file("./test_matrix/pr05_answer.txt")
    expected_answer = Answer.One
    expected_system = {"x1": "1", "x2": "-1", "x3": "3", "x4": "4"}

    eliminated_matrix = Gauss_Jordan_elimination(original_matrix)

    assert matrices_are_equal(eliminated_matrix, expected_matrix)

    answer, system = find_system_solution(eliminated_matrix)

    assert answer == expected_answer
    assert system == expected_system
