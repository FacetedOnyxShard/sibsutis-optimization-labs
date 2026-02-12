from fraction import Fraction
from operator import itemgetter
from sympy import symbols, sympify, Add, solve, Eq
from enum import Enum
import json


def read_matrix_from_file(filename: str) -> list[list[Fraction]]:
    with open(filename) as file:
        matrix = []
        for line in file:
            matrix.append(list(map(Fraction.to_fraction, line.split())))

    return matrix


def print_matrix(matrix: list[list[Fraction]]) -> None:
    for row in matrix:
        print(" ".join(f"{str(fraction):>10}" for fraction in row))
    print()


def transform_matrix(
    matrix: list[list[Fraction]], row: int, col: int
) -> list[list[Fraction]]:
    transformed_matrix = copy_matrix(matrix)
    enabling_element = matrix[row][col]

    for j in range(len(matrix[row])):
        transformed_matrix[row][j] = matrix[row][j] / enabling_element

    for i in range(len(matrix)):
        if i == row:
            continue
        transformed_matrix[i][col] = Fraction(0)

    return transformed_matrix


def find_enabling_element(a_matrix: list[list[Fraction]], current_row: int) -> int:
    column = -1

    for j in range(len(a_matrix[current_row])):
        if a_matrix[current_row][j] != Fraction(0):
            column = j
            break

    return column


def copy_matrix(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    matrix_copy = [row[:] for row in matrix]
    return matrix_copy


def calculate_elements(a, a_hat, row: int, col: int):
    enabling_element = a[row][col]

    for crow in range(len(a)):
        koef = a[crow][col] / enabling_element

        for ccol in range(col, len(a[crow])):
            if crow == row:
                continue

            current_element = a[crow][ccol]

            a_hat[crow][ccol] = current_element - (koef * a[row][ccol])


def strike_zero_rows(matrix: list[list[Fraction]], row) -> list[list[Fraction]]:
    zero_rows = []
    for crow in range(row + 1, len(matrix)):
        is_zero = True
        for j in range(len(matrix[crow])):
            if matrix[crow][j] != Fraction(0):
                is_zero = False

        if is_zero:
            zero_rows.append(crow)

    new_matrix = []
    cur_zero_row_idx = 0
    for i, row in enumerate(matrix):
        if len(zero_rows) != 0 and i == zero_rows[cur_zero_row_idx]:
            if cur_zero_row_idx < len(zero_rows) - 1:
                cur_zero_row_idx += 1
            continue

        new_matrix.append(row)

    return new_matrix


def swap_rows(matrix, row1, row2):
    if not (0 <= row1 < len(matrix) and 0 <= row2 < len(matrix)):
        raise IndexError()

    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp


def select_main_element(matrix, cur_row):
    ccol = 0
    ccol_abs_elem_and_idxs = []

    for ccol in range(len(matrix[0])):
        for crow in range(cur_row, len(matrix)):
            ccol_abs_elem_and_idxs.append((abs(matrix[crow][ccol]), crow))

        max_abs_elem_and_idx = max(ccol_abs_elem_and_idxs, key=itemgetter(0))
        if max_abs_elem_and_idx[0] != Fraction(0):
            break

    swap_rows(matrix, cur_row, max_abs_elem_and_idx[1])

    return ccol


def write_intermediate_matrix_to_file(filepath: str, matrix: list[list[Fraction]]):
    with open(filepath, "a") as file:
        for i, row in enumerate(matrix):

            for j, item in enumerate(matrix[i]):
                if j == 0:
                    file.write(f"{str(item)}")
                    continue

                file.write(f"{str(item):>10}")

            if i + 1 == len(matrix):
                file.write("\n\n")
            else:
                file.write("\n")


def Gauss_Jordan_elimination(
    original_matrix: list[list[Fraction]], show_intermediate=0
):
    a = copy_matrix(original_matrix)

    for row in range(len(a)):
        if row >= len(a):
            break

        col = select_main_element(a, row)
        # col = find_enabling_element(a, row) # нужна если
        # # не используется select_main_element

        a_hat = transform_matrix(a, row, col)
        calculate_elements(a, a_hat, row, col)
        a_hat = strike_zero_rows(a_hat, row)
        a = copy_matrix(a_hat)

        if show_intermediate:
            write_intermediate_matrix_to_file("./matrix.txt", a)

    return a


def have_incorrect_row(matrix: list[list[Fraction]]):
    res = False

    for i in range(len(matrix)):
        is_zero_row = True
        last_element_in_row = matrix[i][-1]
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] != Fraction(0):
                is_zero_row = False
                break

        if is_zero_row and last_element_in_row != Fraction(0):
            res = True
            break

    return res


def is_identity_matrix(matrix: list[list[Fraction]]):
    current_k = 0
    if len(matrix) != len(matrix[0]) - 1:
        return False

    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            if j == current_k:
                if not matrix[i][j] == Fraction(1):
                    return False
            else:
                if not matrix[i][j] == Fraction(0):
                    return False
        current_k += 1

    return True


def frac_to_sympy(n: Fraction):
    return sympify(str(n))


def find_common_solution(matrix: list[list[Fraction]]):
    solutions = []
    for i, row in enumerate(matrix):
        # можно создавать выражение только 1 раз
        expression = create_linear_expression(len(row) - 1)
        equation = Eq(expression, frac_to_sympy(row[-1]))
        free_var_idx = -1
        free_var_found = False

        for j, value in enumerate(row):
            if j == len(row) - 1:  # нужно для того, чтобы не включать расширенную часть
                continue  # можно написать break
            if not free_var_found and value == Fraction(1):
                free_var_idx = j + 1
                free_var_found = True

            equation = equation.subs(f"k{j + 1}", frac_to_sympy(value))

        solution = solve(equation, f"x{free_var_idx}")
        solutions.append((f"x{free_var_idx}", solution[0]))

    return solutions


class Answer(str, Enum):
    No = "нет решений"
    One = "одно решение"
    Infinity = "бесконечно много решений"


def find_system_solution(matrix: list[list[Fraction]]):
    answer = Answer.No
    answer_system = {}

    if have_incorrect_row(matrix):
        pass
    elif is_identity_matrix(matrix):
        answer = Answer.One
        for i, row in enumerate(matrix, start=1):
            key = f"x{i}"
            answer_system[key] = str(row[-1])
    else:
        answer = Answer.Infinity
        solutions = find_common_solution(matrix)
        for key, value in solutions:
            answer_system[key] = value

    return (answer, answer_system)


def write_answer_to_file(filepath: str, answer_object):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(answer_object, file)


def solve_linear_system(matrix: list[list[Fraction]]) -> None:
    eliminated_matrix = Gauss_Jordan_elimination(matrix, 1)

    answer, answer_system = find_system_solution(eliminated_matrix)

    answer_object = {"answer": str(answer), "answer_system": answer_system}
    write_answer_to_file("./answer.json", answer_object)


def matrices_are_equal(
    matrix1: list[list[Fraction]], matrix2: list[list[Fraction]]
) -> bool:
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True


def create_linear_expression(n: int):
    var_symbols = symbols([f"x{i + 1}" for i in range(n)])
    coef_symbols = symbols([f"k{i + 1}" for i in range(n)])

    terms = [coef * var for coef, var in zip(coef_symbols, var_symbols)]
    expression = Add(*terms)
    return expression


def truncate_file(filepath: str):
    with open(filepath, "w"):
        pass


def main() -> None:
    matrix = read_matrix_from_file("test_matrix/pr01_task.txt")

    truncate_file("./matrix.txt")

    solve_linear_system(matrix)


if __name__ == "__main__":
    main()
