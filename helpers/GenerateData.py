from faker import Faker

class GenerateUser:
    """ Fake providers are here: https://faker.readthedocs.io/en/master/providers.html
    """

    fake = Faker()

    def first_name(self):
        name = self.fake.first_name()
        return name

    def last_name(self):
        name = self.fake.last_name()
        return name

    def full_name(self):
        full_name = self.fake.first_name()
        return full_name

    def zip_code(self):
        id_code = self.fake.postcode()
        return id_code

    def email(self):
        lemberg_email = str(self.first_name() + self.last_name() + "@test.co.uk")
        return lemberg_email

    def address(self):
        address = self.fake.address()
        return address

    def city(self):
        city = self.fake.city()
        return city

    def phone_number(self):
        phone_number = self.fake.phone_number().split('x')[0]
        return phone_number

    def birth_day(self):
        birth_date = f'{self.fake.date_of_birth():%m/%d/%Y}'
        return birth_date
