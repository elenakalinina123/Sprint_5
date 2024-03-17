from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationPage:
    ALL_INPUTS = (By.XPATH, ".//div/input")
    DIV_FORM_BUTTON = (By.XPATH, ".//div/form/button")
    CLASS_INPUT_ERROR = (By.CLASS_NAME, "input__error")

    BASE_LINK = 'https://stellarburgers.nomoreparties.site/'

    def test_valid_registration(self, driver, name, username, password):
        driver.get(self.BASE_LINK + 'register')

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(self.ALL_INPUTS))

        elements = driver.find_elements(*self.ALL_INPUTS)

        name_field, username_field, password_field = elements

        name_field.send_keys(name)
        username_field.send_keys(username)
        password_field.send_keys(password)

        register_button = driver.find_element(*self.DIV_FORM_BUTTON)
        register_button.click()

        WebDriverWait(driver, 3).until(
            EC.url_contains("/login"))

        url = driver.current_url

        assert "/login" in url

        driver.quit()

    def test_registration_short_password(self, driver, name,
                                         username, password_short):
        driver.get(self.BASE_LINK + 'register')

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(self.ALL_INPUTS))
        elements = driver.find_elements(*self.ALL_INPUTS)
        name_field, username_field, password_field = elements

        name_field.send_keys(name)
        username_field.send_keys(username)
        password_field.send_keys(password_short)

        register_button = driver.find_element(*self.DIV_FORM_BUTTON)
        register_button.click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            self.CLASS_INPUT_ERROR)).text == "Некорректный пароль"

        driver.quit()
