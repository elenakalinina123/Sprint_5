import pytest
from utils import password_generator, username_generator

from selenium import webdriver


@pytest.fixture
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="session")
def email():
    base_name = "didimadloba"
    mail = "@mail.ge"
    return (username_generator(base_name) + mail)


@pytest.fixture(scope="session")
def password():
    return password_generator(8)


@pytest.fixture
def password_short():
    return password_generator(3)
