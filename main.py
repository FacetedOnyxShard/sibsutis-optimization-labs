from matrix import *


def main() -> None:
    task_id = "lr01"
    matrix = read_matrix_from_file(f"test_matrix/{task_id}_task.txt")

    dir_for_answers = "answer"
    answer_filepath = f"./{dir_for_answers}/answer.json"
    matrices_filepath = f"./{dir_for_answers}/matrix.txt"

    os.makedirs(dir_for_answers, exist_ok=True)
    create_or_truncate_file(matrices_filepath)
    create_or_truncate_file(answer_filepath)

    answer_obj, intermediate_matrices = solve_linear_system(matrix)

    write_answer_to_file(answer_filepath, answer_obj)
    for matrix in intermediate_matrices:
        write_intermediate_matrix_to_file(matrices_filepath, matrix)


if __name__ == "__main__":
    main()
