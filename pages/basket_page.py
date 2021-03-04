from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_be_cant_see_product_in_basket(self):
       assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_BACKET), "Not product in basket"

    def should_be_see_empty_message_in_basket(self):
       assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "See empty message in basket"
  