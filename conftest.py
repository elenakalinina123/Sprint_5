import pytest
from utils import password_generator

from selenium import webdriver


@pytest.fixture
def driver():
    return webdriver.Chrome()


@pytest.fixture
def name():
    return "Анастасия"


@pytest.fixture
def username(scope="session"):
    # username = "kldfjgkldfg"
    username = "didimadloba"
    number = str('147')  # have to change this number for registration test
    mail = "@mail.ge"
    return (username + number + mail)


# @pytest.fixture
# def password(scope="session"):
#     return password_generator(8)

@pytest.fixture
def password(scope="session"):
    return 'madloba123'


@pytest.fixture
def password_short(scope="session"):
    return password_generator(3)
