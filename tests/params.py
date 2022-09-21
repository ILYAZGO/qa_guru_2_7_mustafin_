from faker import Faker
import random
import os

fake = Faker('ru_RU')
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.ascii_company_email()
ten_digits = str(random.randint(1111111111,9999999999))
address = fake.address()

filename = '/resources/kitty.jpeg'
path = os.getcwd() + filename

age = str(random.randint(10,99))
department = fake.color_name()
add_letter = 'a'