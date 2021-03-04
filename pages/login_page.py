from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user(email, password)

    def should_be_login_url(self):
        url=self.browser.current_url
        index = url.find("/login")
        assert index>0, "login is in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login form registration is not presented"
    def register_new_user(self,email, password):
        input_email=self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        input_email.send_keys(email)
        input_email=self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        input_email.send_keys(password)
        input_email=self.browser.find_element(*LoginPageLocators.LOGIN_CONFIRM)
        input_email.send_keys(password)
        button_reg=self.browser.find_element(*LoginPageLocators.BUTTON_REGOSTRATION)
        button_reg.click()
   
