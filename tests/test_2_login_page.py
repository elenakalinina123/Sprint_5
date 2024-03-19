import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginPage:
    EMAIL_INPUT = (
        By.XPATH, ".//div/label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//div/input[@type='password']")

    LOGIN_PAGE = (
        By.XPATH, ".//main/div/form/button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, ".//nav/ul/li/button")
    H2_LOCATOR_LOGIN_PAGE = (By.XPATH, ".//main/div/h2")
    LOGIN_PAGE_BUTTON = (
        By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    PROFILE_PAGE_BUTTON = (By.XPATH, ".//header/nav/a/p")
    FORM_BUTTON = (By.XPATH, ".//form/button")
    H1_LOCATOR = (By.XPATH, ".//main/section/h1")
    CONSTRUCTOR_LOCATOR = (By.XPATH, ".//li/a/p[text()='Конструктор']")

    NEW_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    LOGIN_FROM_REGISTER = (By.XPATH, ".//a[contains(text(), 'Войти')]")

    BASE_LINK = 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_main_page(self, driver, email, password):
        driver.get(self.BASE_LINK)

        login_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE_BUTTON))

        login_page_button.click()

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.NEW_ORDER_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

    def test_login_from_profile(self, driver, email, password):
        driver.get(self.BASE_LINK)

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.NEW_ORDER_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

    @pytest.mark.parametrize("link", ['register', 'forgot-password'])
    def test_login_from_registration_form(self, link, driver,
                                          email, password):
        driver.get(self.BASE_LINK + link)

        login_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_FROM_REGISTER))

        login_page_button.click()

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.FORM_BUTTON))

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.NEW_ORDER_BUTTON))

        assert button.text == "Оформить заказ"
        assert button.is_displayed()

    def test_profile_page(self, driver, email, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
        password_field.send_keys(password)

        login_button.click()

        profile_page_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                self.PROFILE_PAGE_BUTTON))

        profile_page_button.click()

        button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON))

        assert button.is_displayed() is True

    def test_profile_to_constructor(self, driver, email, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
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

    def test_logout(self, driver, email, password):
        driver.get(self.BASE_LINK + 'login')

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(self.LOGIN_PAGE))

        email_field = driver.find_element(*self.EMAIL_INPUT)
        password_field = driver.find_element(*self.PASSWORD_INPUT)

        email_field.send_keys(email)
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
