import runner
import helper
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
        str_value += f'Valid => {self.is_valid}'
        return str_value

    def __repr__(self):
        return str(self)

    @property
    def is_valid(self):
        return self.birth_year is not None \
               and self.issue_year is not None \
               and self.expiry_year is not None \
               and self.height is not None \
               and self.hair_color is not None \
               and self.eye_color is not None \
               and self.passport_id is not None
        # and self.country_id is not None


passports = [Passport(x) for x in argv]


def part1(data):
    return len([p for p in passports if p.is_valid])
