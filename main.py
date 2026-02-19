from matrix import *


def main() -> None:
    TASK_ID = "lr02_01"
    MATRIX_DIR = "test_matrix"

    MATRIX = read_matrix_from_file(f"{MATRIX_DIR}/{TASK_ID}_task.txt")

    DIR_FOR_ANSWERS = "answer"
    ANSWERS_FILEPATH = f"./{DIR_FOR_ANSWERS}/answer.json"

    os.makedirs(DIR_FOR_ANSWERS, exist_ok=True)
    create_or_truncate_file(ANSWERS_FILEPATH)

    answer_obj, intermediate_matrices = solve_linear_system(MATRIX)

    full_answer = {}
    for matrix in intermediate_matrices:
        key, value = convert_matrix_to_json_field(matrix)
        full_answer[key] = value
    full_answer["solution"] = answer_obj

    write_answer_to_file(ANSWERS_FILEPATH, full_answer)


if __name__ == "__main__":
    main()
