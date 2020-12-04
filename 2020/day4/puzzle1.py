import utils


class Passport(object):
    def __init__(self,
                 pid: int,
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


def main():
    number_of_valid_passorts = 0
    passport_details = utils.read_input_file("passport_details.txt")
    for passport_detail in passport_details:
        try:
            Passport(**passport_detail)
        except TypeError:
            pass
        else:
            number_of_valid_passorts += 1
    print(f"Valid passports found: {number_of_valid_passorts}")


if __name__ == "__main__":
    main()
