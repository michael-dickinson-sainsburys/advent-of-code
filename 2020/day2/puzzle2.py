import utils


def characters_are_the_same(first_character, second_character):
    return first_character == second_character


input_values_from_file = utils.read_input_file(filename="input.txt")
input_values = [x.strip().split(" ") for x in input_values_from_file]
things_to_test = [
    {
        "first_occurence": int(x[0].split("-")[0]) - 1,
        "second_occurence": int(x[0].split("-")[1]) - 1,
        "character": x[1][0],
        "password": x[2]
    }
    for x in input_values
]
valid_passwords = 0
for thing in things_to_test:
    if characters_are_the_same(thing['character'], thing['password'][thing['first_occurence']]) ^ characters_are_the_same(thing['character'], thing['password'][thing['second_occurence']]):
        valid_passwords += 1
    else:
        print(f"Password {thing['password']} does not meet password policy")

print(f"Number of valid passwords: {valid_passwords}")
