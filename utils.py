import secrets
import string


def password_generator(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
