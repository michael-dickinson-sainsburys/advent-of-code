import utils


def main():
    grouped_answers = utils.read_input_file("customs_declaration_form_questions.txt")
    print(f"grouped_answers = {grouped_answers}")
    sum_of_counts = 0
    sets_of_answers = [[{x for x in y} for y in z if y] for z in grouped_answers]
    for set_of_answers in sets_of_answers:
        combined_answers = set_of_answers.pop()
        for answer in set_of_answers:
            combined_answers.intersection_update(answer)
        sum_of_counts += len(combined_answers)
    print(f"Sum of counts: {sum_of_counts}")


if __name__ == "__main__":
    main()
