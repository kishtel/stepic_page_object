import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
link = "http://selenium1py.pythonanywhere.com/"
@pytest.mark.need_review
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          #
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_should_see_login_url(self,browser):
        #link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()    
    
    def test_guest_should_see_login_form(self,browser):  
        #link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form
    
    def test_guest_should_see_login_register(self,browser):
        #link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        page.button_basket_click()
        basket_page=BasketPage(browser, browser.current_url)
        basket_page.should_be_cant_see_product_in_basket()
        basket_page.should_be_see_empty_message_in_basket()
        
    
    
    