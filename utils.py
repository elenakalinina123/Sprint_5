import secrets
import string
from datetime import datetime


def password_generator(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def username_generator(base_name):
    numbers = string.digits

    date_time = datetime.now().strftime("%d%M")
    random_part = ''.join(secrets.choice(numbers) for i in range(4))
    username = base_name + date_time + random_part

    return username
