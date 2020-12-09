import re

import utils

COUNTER = 1


def main(bag_colour: str):
    rules = utils.read_input_file("baggage_rules.txt")
    print(len(bags_that_can_hold_bags(bag_colour, rules)))


def bags_that_can_hold_bags(bag_colour, rules):
    print(f"Checking for colour: {bag_colour}")
    global COUNTER
    pattern = re.compile(f"^([a-zA-Z0-9 ]+) bags contain [a-zA-Z0-9, ]+{bag_colour}[a-zA-Z0-9, ]+.$")
    outer_bag_colours = list()
    for rule in rules:
        outer_bag_colours.extend(pattern.findall(rule))
    print(f"Pass {COUNTER}: outer_bag_colours = {outer_bag_colours}")
    COUNTER += 1
    temp = list()
    for colour in outer_bag_colours:
        temp.extend(bags_that_can_hold_bags(colour, rules))
    return set(outer_bag_colours + temp)


if __name__ == "__main__":
    main(bag_colour="shiny gold bag")
