import utils


def main():
    grouped_answers = utils.read_input_file("customs_declaration_form_questions.txt")
    sum_of_counts = 0
    for group_answers in grouped_answers:
        combined_answers = set([x for z in group_answers for y in z for x in y])
        sum_of_counts += len(combined_answers)
    print(f"Sum of counts: {sum_of_counts}")


if __name__ == "__main__":
    main()
