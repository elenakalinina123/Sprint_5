import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginPage:
    ALL_INPUTS = (By.XPATH, ".//div/input")

    LOGIN_PAGE = (
        By.XPATH, ".//main/div/form/button[contains(text(), 'Войти')]")
    LOGIN_PAGE_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")
    LOGOUT_BUTTON = (By.XPATH, ".//nav/ul/li/button")
    H2_LOCATOR_LOGIN_PAGE = (By.XPATH, ".//main/div/h2")
    LARGE_BLUE_BUTTON = (By.CLASS_NAME, "button_button_size_large__G21Vg")
    PROFILE_PAGE_BUTTON = (By.XPATH, ".//header/nav/a/p")
    FORM_BUTTON = (By.CSS_SELECTOR, "form button")
    H1_LOCATOR = (By.XPATH, ".//main/section/h1")
    CONSTRUCTOR_LOCATOR = (By.XPATH, ".//li/a/p[text()='Конструктор']")

    BASE_LINK = 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_main_page(self, driver, username, password):
        driver.get(self.BASE_LINK)

        login_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LARGE_BLUE_BUTTON))

        login_page_button.click()

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LARGE_BLUE_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

        driver.quit()

    def test_login_from_profile(self, driver, username, password):
        driver.get(self.BASE_LINK)

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LARGE_BLUE_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

        driver.quit()

    @pytest.mark.parametrize("link", ['register', 'forgot-password'])
    def test_login_from_registration_form(self, link, driver,
                                          username, password):
        driver.get(self.BASE_LINK + link)

        login_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE_BUTTON))

        login_page_button.click()

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LARGE_BLUE_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

        driver.quit()

    def test_profile_page(self, driver, username, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON))

        assert button.is_displayed() is True

        driver.quit()

    def test_profile_to_constructor(self, driver, username, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        constructor_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.CONSTRUCTOR_LOCATOR))

        constructor_button.click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            self.H1_LOCATOR)).text == "Соберите бургер"

        driver.quit()

    def test_logout(self, driver, username, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        username_field, password_field = driver.find_elements(*self.ALL_INPUTS)

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            self.H2_LOCATOR_LOGIN_PAGE)).text == "Вход"

        driver.quit()
