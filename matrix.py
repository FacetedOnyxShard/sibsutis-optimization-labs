from fraction import Fraction
import copy
from operator import itemgetter


def read_matrix_from_file(filename: str) -> list[list[Fraction]]:
    with open(filename) as file:
        matrix = []
        for line in file:
            matrix.append(list(map(Fraction, map(int, line.split()))))

    return matrix


def print_matrix(matrix: list[list[Fraction]]) -> None:
    for row in matrix:
        print(" ".join(f"{str(fraction):>10}" for fraction in row))
    print()


def transform_matrix(matrix: list[list[Fraction]], row: int, col: int):
    transformed_matrix = matrix_copy(matrix)
    enabling_element = matrix[row][col]

    for j in range(len(matrix[row])):
        transformed_matrix[row][j] = matrix[row][j] / enabling_element

    for i in range(len(matrix)):
        if i == row:
            continue
        transformed_matrix[i][col] = Fraction(0)

    return transformed_matrix


def find_enabling_element(a_matrix: list[list[Fraction]], current_row: int):
    column = -1

    for j in range(len(a_matrix[current_row])):
        if a_matrix[current_row][j] != Fraction(0):
            column = j
            break

    return column


def matrix_copy(matrix):
    matrix_copy = [row[:] for row in matrix]
    return matrix_copy


def calculate_elements(a, a_hat, row, col):
    enabling_element = a[row][col]

    for crow in range(len(a)):
        koef = a[crow][col] / enabling_element

        for ccol in range(col, len(a[crow])):
            if crow == row:
                continue

            current_element = a[crow][ccol]

            a_hat[crow][ccol] = current_element - (koef * a[row][ccol])


def strike_zero_rows(matrix, row) -> list[list[Fraction]]:
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


def Gauss_Jordan_elimination(original_matrix):
    a = matrix_copy(original_matrix)

    for row in range(len(a)):
        if row >= len(a):
            break

        col = select_main_element(a, row)
        # col = find_enabling_element(a, row) # нужна если
        # # не используется select_main_element

        a_hat = transform_matrix(a, row, col)
        calculate_elements(a, a_hat, row, col)
        a_hat = strike_zero_rows(a_hat, row)
        a = matrix_copy(a_hat)

    # нужно выводить промежуточные матрицы,
    # после каждого шага исключений

    # нужно получать
    # либо бесконечно много решений и выводить общее решение
    # либо нет решений
    # либо одно решение находить его и выводить переменные

    return a


def FractionMatrixEqual(m1, m2) -> bool:
    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i][j] != m2[i][j]:
                return False

    return True


def main() -> None:
    matrix = [[0 for _ in range(10)] for _ in range(10)]

    for col in range(len(matrix[1])):
        matrix[1][col] = 1

    second_row = matrix[1]

    for col in range(len(second_row)):
        second_row[col] = 10

    print(matrix)


if __name__ == "__main__":
    main()
