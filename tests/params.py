from faker import Faker
import random
import os

fake = Faker('ru_RU')
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.ascii_company_email()
mobile = random.randint(1111111111,9999999999)
address = fake.address()

filename = '/testdata/kitty.jpeg'
path = os.getcwd() + filename