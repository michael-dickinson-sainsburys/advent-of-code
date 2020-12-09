import utils


def main(bag_colour):
    number_of_bags_needed = 0
    rules = utils.read_input_file("baggage_rules.txt")
    bags = dict()
    for rule in rules:
        bags.update(get_bags_in_bag(rule))
    my_bag_contains = sum([int(x[0]) for x in bags[bag_colour]])
    print(my_bag_contains)
    return number_of_bags_needed


def get_bags_in_bag(rule):
    outer_bag_colour, contents = rule.split(" bags contain ")
    contained_bags = [
        (bag.split(" ")[0], " ".join(bag.strip(" bags").split(" ")[1:]))
        for bag in contents.strip(".\n").split(", ")
    ]
    return {outer_bag_colour: contained_bags}


if __name__ == "__main__":
    main("shiny gold")
