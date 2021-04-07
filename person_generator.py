import random


class PersonGenerator:
    """Generates random data for managing family/personal accounts"""

    def __init__(self):
        self.domains = ('gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'icloud.com', 'aol.com')
        self.password_length = 10
        try:
            self.first_names = open('first_names.txt').read().splitlines()
            self.last_names = open('last_names.txt').read().splitlines()
            self.nicknames = open('nicknames.txt').read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError('One or several dictionaries files are missing.')

    @staticmethod
    def get_random_line(obj):
        """Picks a random line from file"""
        line = random.choice(obj)
        return line

    def generate_email(self) -> str:
        """Generate random email based on wordlist and randomize symbols"""
        nickname = self.get_random_line(self.nicknames)
        if random.choice((True, False)):
            nickname += str(random.randint(1, 999))
        else:
            if 'o' in nickname:
                nickname = nickname.replace('o', '0', 1)
            elif 'i' in nickname:
                nickname = nickname.replace('i', '1', 1)

        domain = random.choice(self.domains)
        return '{0}@{1}'.format(nickname, domain)

    def generate_password(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@-*1234567890"
        password = ''
        for i in range(self.password_length + 1):
            password += random.choice(characters)
        return password

    def generate_person(self, members: int, family=True) -> list:
        """Generate one or several persons, it may be family or not."""
        if family:
            last_name = self.get_random_line(self.last_names)
        persons = []
        for person in range(1, members + 1):
            if not family:
                last_name = self.get_random_line(self.last_names)
            persons.append({
                'First Name': self.get_random_line(self.first_names),
                'Last Name': last_name,
                'Email': self.generate_email(),
                'Password': self.generate_password()
            })
        return persons

    def get_cli_output(self, members):
        persons = self.generate_person(members)
        for item in persons:
            print('{0}\n{1}\n{2}\n{3}\n{2};{3}\n'.format(
                item.get('First Name'),
                item.get('Last Name'),
                item.get('Email'),
                item.get('Password')
            ))


prs = PersonGenerator()

print(prs.get_cli_output(6))
