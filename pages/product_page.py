from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def should_be_submit_page(self):
        self.should_be_product_url()
        self.should_be_product_form()
        self.should_be_submit_form()
        
 
    def go_to_product_page(self):
         link = self.browser.find_element(*ProductPageLocators.BUTTON_SUBMIT)
         link.click()
         self.solve_quiz_and_get_code()

    def should_be_product_url(self):
        url=self.browser.current_url
        index = url.find("/?promo=newYear")
        assert index>0, "login is in current url"

    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM), "Product form is not presented"
    
    def should_be_submit_form(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_SUBMIT), "Button submit is not presented"
      
    def should_be_see_name_add_basket(self,prod_name):
        prod_name_basket_el=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BACKET)
        prod_name_basket=prod_name_basket_el.text
        print(prod_name_basket)
        assert prod_name==prod_name_basket,"Text add to backet"

    def should_be_equil_price_backet(self,price_book):
        price_backet_el=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BACKET)
        price_backet=price_backet_el.text
        print(price_backet)
        assert price_book==price_backet,"Price main equil price backet"
    def return_price_main(self):
        price_book_el=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MAIN)
        price_book=price_book_el.text
        print(price_book)
        return price_book
    def return_name_book(self):
        prod_name_el=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        prod_name=prod_name_el.text
        print(prod_name)
        return prod_name   
