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


def Gauss_Jordan_elimination(original_matrix):
    a = matrix_copy(original_matrix)

    for row in range(len(a)):
        col = find_enabling_element(a, row)
        a_hat = transform_matrix(a, row, col)
        calculate_elements(a, a_hat, row, col)
        a = matrix_copy(a_hat)

    # нужно добавить вычеркивание строк, состоящих из 0

    # нужно получать
    # либо бесконечно много решений и выводить общее решение
    # либо нет решений
    # либо одно решение находить его и выводит переменные

    return a_hat


def FractionMatrixEqual(m1, m2) -> bool:
    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i][j] != m2[i][j]:
                return False

    return True


# def main() -> None:
#     original_matrix = read_matrix_from_file("test_matrix/pr01.txt")

#     print("Результат:")
#     print_matrix(a)

#     print("Ожидаемое значение:")
#     print_matrix(expected_matrix_after_first_transform)


# if __name__ == "__main__":
#     main()
