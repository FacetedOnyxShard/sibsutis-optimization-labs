from fraction import Fraction
import copy


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
    transformed_matrix = copy_matrix(matrix)
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


def copy_matrix(matrix: list[list[Fraction]]):
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


def Gauss_Jordan_elimination(original_matrix):
    a = copy_matrix(original_matrix)

    for row in range(len(a)):
        if row >= len(a):
            break
        col = find_enabling_element(a, row)
        a_hat = transform_matrix(a, row, col)
        calculate_elements(a, a_hat, row, col)
        a_hat = strike_zero_rows(a_hat, row)
        a = copy_matrix(a_hat)

    # нужно получать
    # либо бесконечно много решений и выводить общее решение
    # либо нет решений
    # либо одно решение находить его и выводит переменные

    return a


def matrices_are_equal(
    matrix1: list[list[Fraction]], matrix2: list[list[Fraction]]
) -> bool:
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True


def main() -> None:
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


if __name__ == "__main__":
    main()
