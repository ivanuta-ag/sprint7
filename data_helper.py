import random
import string
from datetime import datetime

main_url = 'https://qa-scooter.praktikum-services.ru'
post_courier = f'{main_url}/api/v1/courier'
del_courier = f'{main_url}/api/v1/courier/:id'
login_courier = f'{main_url}/api/v1/courier/login'
create_order= f'{main_url}/api/v1/orders'


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_numbers(length):
    numbs = '0123456789'
    random_nums = ''.join(random.choice(numbs) for i in range(length))
    return random_nums

