import re

import utils


class Passport(object):
    def __init__(self,
                 pid: str,
                 byr: int,
                 iyr: int,
                 eyr: int,
                 hgt: str,
                 hcl: str,
                 ecl: str,
                 cid: int = None):
        self.birth_year = byr
        self.issue_year = iyr
        self.expiration_year = eyr
        self.height = hgt
        self.hair_colour = hcl
        self.eye_colour = ecl
        self.passport_id = pid
        self.country_id = cid
        self.valid_eye_colours = ["amb", "blu", "brn", "gry",
                                  "grn", "hzl", "oth"]
        self.validate()

    def validate(self):
        if int(self.birth_year) < 1920 or int(self.birth_year) > 2002:
            raise TypeError("Invalid birth year")
        if int(self.issue_year) < 2010 or int(self.issue_year) > 2020:
            raise TypeError("Invalid issue year")
        if int(self.expiration_year) < 2020 or int(self.expiration_year) > 2030:
            raise TypeError("Invalid expiration year")
        if not isinstance(self.height, str):
            print(type(self.height))
            raise TypeError("Invalid height1")
        elif not re.match("(cm|in)", self.height[-2:]):
            raise TypeError("Invalid height2")
        elif self.height[-2:] == "cm":
            if int(self.height[:-2]) < 150 or int(self.height[:-2]) > 193:
                raise TypeError("Invalid height3")
        elif self.height[-2:] == "in":
            if int(self.height[:-2]) < 59 or int(self.height[:-2]) > 76:
                raise TypeError("Invalid height4")
        else:
            raise TypeError("Invalid height5")
        if not re.match("#[0-9a-f]{6}", self.hair_colour):
            raise TypeError("Invalid hair colour")
        if self.eye_colour not in self.valid_eye_colours:
            raise TypeError("Invalid eye colour")
        if len(self.passport_id) != 9:
            raise TypeError("Invalid passport id")


def main():
    number_of_valid_passports = 0
    passport_details = utils.read_input_file("passport_details.txt")
    for passport_detail in passport_details:
        try:
            Passport(**passport_detail)
        except TypeError as e:
            print(passport_detail)
            print(e)
        else:
            number_of_valid_passports += 1
    print(f"Valid passports found: {number_of_valid_passports}")


if __name__ == "__main__":
    main()
