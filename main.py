from fraction import Fraction

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

def main() -> None:
    matrix = read_matrix_from_file("matrix_examples/matrix1.txt")

    print("Исходная матрица:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()