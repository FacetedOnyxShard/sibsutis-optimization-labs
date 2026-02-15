from matrix import *


def main() -> None:
    task_id = "pr04"
    matrix = read_matrix_from_file(f"test_matrix/{task_id}_task.txt")

    dir_for_answers = "answer"
    answer_filepath = f"./{dir_for_answers}/answer.json"

    os.makedirs(dir_for_answers, exist_ok=True)
    create_or_truncate_file(answer_filepath)

    answer_obj, intermediate_matrices = solve_linear_system(matrix)

    full_answer = {}
    for matrix in intermediate_matrices:
        key, value = convert_matrix_to_json_field(matrix)
        full_answer[key] = value
    full_answer["solution"] = answer_obj

    write_answer_to_file(answer_filepath, full_answer)


if __name__ == "__main__":
    main()
