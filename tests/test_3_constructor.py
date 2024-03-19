import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    BASE_LINK = 'https://stellarburgers.nomoreparties.site/'

    SAUCE = (By.XPATH, ".//div/span[text()='Соусы']")
    BUNS = (By.XPATH, ".//div/span[text()='Булки']")
    FILLINGS = (By.XPATH, ".//div/span[text()='Начинки']")

    SAUCE_DIV = (By.XPATH, ".//div/span[text()='Соусы']/parent::div")
    BUNS_DIV = (By.XPATH, ".//div/span[text()='Булки']/parent::div")
    FILLINGS_DIV = (By.XPATH, ".//div/span[text()='Начинки']/parent::div")

    locators = [
        (SAUCE, SAUCE_DIV),
        (FILLINGS, FILLINGS_DIV)
    ]

    @pytest.mark.parametrize("test_object", locators)
    def test_constructor(self, driver, test_object):
        driver.get(self.BASE_LINK)

        button_locator = test_object[0]
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(button_locator))
        button.click()

        div_locator = test_object[1]
        div = driver.find_element(*div_locator)

        div_class = div.get_attribute('class')

        assert 'current' in div_class

    def test_constructor_buns(self, driver):
        driver.get(self.BASE_LINK)

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.SAUCE))
        button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.BUNS))
        button.click()

        div = driver.find_element(*self.BUNS_DIV)

        div_class = div.get_attribute('class')

        assert 'current' in div_class
