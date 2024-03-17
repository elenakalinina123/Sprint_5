import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    BASE_LINK = 'https://stellarburgers.nomoreparties.site/'

    SAUCE_TEXT = (By.XPATH, ".//div/h2[text()='Соусы']")
    BUNS_TEXT = (By.XPATH, ".//div/h2[text()='Булки']")
    FILLINGS_TEXT = (By.XPATH, ".//div/h2[text()='Начинки']")

    SAUCE = (By.XPATH, ".//div/span[text()='Соусы']")
    BUNS = (By.XPATH, ".//div/span[text()='Булки']")
    FILLINGS = (By.XPATH, ".//div/span[text()='Начинки']")

    parameter = [
        (SAUCE, SAUCE_TEXT, 'Соусы'),
        # (BUNS, BUNS_TEXT, 'Булки'),
        (FILLINGS, FILLINGS_TEXT, 'Начинки')
    ]

    @pytest.mark.parametrize("test_object", parameter)
    def test_constructor(self, driver, test_object):
        driver.get(self.BASE_LINK)

        link_locator = test_object[0]
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(link_locator))
        button.click()

        text_locator = test_object[1]

        h2 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(text_locator)
        )

        assert h2.text == test_object[2]

        driver.quit()

    def test_constructor_buns(self, driver):
        driver.get(self.BASE_LINK)

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.SAUCE))
        button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.BUNS))
        button.click()

        h2 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(self.BUNS_TEXT)
        )

        assert h2.text == 'Булки'

        driver.quit()
