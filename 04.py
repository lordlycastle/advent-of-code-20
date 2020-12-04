import runner
import re

raw = runner.get_data(4)
argv = [str(x) for x in raw.split('\n\n')]


class Field:
    regex = r'(.+):(.+)'

    def __init__(self, raw):
        self.raw = raw
        self.matches = re.match(Field.regex, raw)
        if len(self.matches.groups()) != 2:
            print(f'Did not find expected groups. Group count: {len(self.matches.groups())}. Raw: {self.raw}')
            return
        self.key = self.matches.group(1)
        self.value = self.matches.group(2)

    def __str__(self):
        return f'{self.key}: {self.value} => {self.raw}'


class Passport:
    keys = {
        'byr': 'birth_year',
        'iyr': 'issue_year',
        'eyr': 'expiry_year',
        'hgt': 'height',
        'hcl': 'hair_color',
        'ecl': 'eye_color',
        'pid': 'passport_id',
        'cid': 'country_id',
    }

    def __init__(self, string_blob):
        self.raw = string_blob
        self.fields = [Field(f) for f in re.split(r' |\n', string_blob)]
        # Default None values. Also need to IDE of class props.
        self.birth_year = None
        self.issue_year = None
        self.expiry_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None
        # Parsed values
        for field in self.fields:
            if field.key not in Passport.keys:
                print(f'This field key: {field} does not exit.')
            else:
                setattr(self, Passport.keys[field.key], field.value)

    def __str__(self):
        str_value = ''
        for (key, value) in Passport.keys.items():
            str_value += f'{value}: {getattr(self, value)} \n'
        str_value += f'P1 Valid => {self.is_valid_p1} \n'
        str_value += f'P2 Valid => {self.is_valid_p2}'
        return str_value

    def __repr__(self):
        return str(self)

    @property
    def is_valid_p1(self):
        """
        Checks all the conditions for part 1.
        :return:
        """
        return (self.birth_year
                and self.issue_year
                and self.expiry_year
                and self.height
                and self.hair_color
                and self.eye_color
                and self.passport_id
                # and self.country_id
                )

    @property
    def is_valid_p2(self):
        """
        Checks all the conditions for part 2 are met. Each line is the condition of that field.
        :rtype: bool
        :return: bool
        """
        return (self.is_valid_p1
                and re.fullmatch(r'\d{4}', self.birth_year) and 2002 >= int(self.birth_year) >= 1920
                and re.fullmatch(r'\d{4}', self.issue_year) and 2010 <= int(self.issue_year) <= 2020
                and re.fullmatch(r'\d{4}', self.expiry_year) and 2020 <= int(self.expiry_year) <= 2030
                and re.fullmatch(r'^\d+(cm|in)$', self.height) and (
                    150 <= int(str(self.height)[:-2]) <= 193  # cm
                    if str(self.height).endswith('cm')
                    else 59 <= int(str(self.height)[:-2]) <= 76  # in
                )
                and re.fullmatch(r'#[0-9a-f]{6}', self.hair_color)
                and self.eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                and re.fullmatch(r'[0-9]{9}', self.passport_id))


passports = [Passport(x) for x in argv]


def part1(data):
    return len([p for p in passports if p.is_valid_p1])


def part2(data):
    return len([p for p in passports if p.is_valid_p2])
