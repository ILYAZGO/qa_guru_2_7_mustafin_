from faker import Faker
import random
import os


fake = Faker('ru_RU')
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.ascii_company_email()
ten_digits = str(random.randint(1111111111, 9999999999))
day = '7'
month = 'June'
year = '1987'
subject1 = 'so'
subject2 = 'ch'
address = fake.address()

state = 'Uttar Pradesh'
city = 'Agra'

filename = os.path.abspath('../resources/kitty.jpeg')

age = str(random.randint(10, 99))
department = fake.color_name()
letter = 'a'

