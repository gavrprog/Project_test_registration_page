from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL is not contains 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Register FORM is not present"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTR).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT).click()