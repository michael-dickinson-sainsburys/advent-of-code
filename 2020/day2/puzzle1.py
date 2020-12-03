import utils

input_values_from_file = utils.read_input_file(filename="input.txt")
input_values = [x.strip().split(" ") for x in input_values_from_file]
things_to_test = [
    {
        "min_occurences": int(x[0].split("-")[0]),
        "max_occurences": int(x[0].split("-")[1]),
        "character": x[1][0],
        "password": x[2]
    }
    for x in input_values
]
valid_passwords = 0
for thing in things_to_test:
    number_of_characters_in_password = \
        thing['password'].count(thing['character'])
    if number_of_characters_in_password < thing['min_occurences'] or \
            number_of_characters_in_password > thing['max_occurences']:
        print(f"Password {thing['password']} does not meet password policy")
    else:
        valid_passwords += 1

print(f"Number of valid passwords: {valid_passwords}")
