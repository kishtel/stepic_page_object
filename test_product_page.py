import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
     @pytest.fixture(scope="function", autouse=True)
     def setup(self,browser):
         link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
         self.page_login = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
         self.page_login.open()
         email = str(time.time()) + "@fakemail.org"
         self.page_login.register_new_user(email, "Tt11Kk224")
         self.page_login.should_be_authorized_user

     def test_user_can_add_product_to_basket(self,browser):
       # ваша реализация теста
         #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
         page = ProductPage(browser, link)
         page.open()
         price_book=page.return_price_main()
         name_book=page.return_name_book()
         page.go_to_product_page_user()
         time.sleep(2)
         page.should_be_see_name_add_basket(name_book)
         page.should_be_equil_price_backet(price_book)
     def test_user_cant_see_success_message(self,browser):
         #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
         page = ProductPage(browser, link)
         page.open()
         page.button_basket_click()
         basket_page=BasketPage(browser, browser.current_url)
         basket_page.should_be_cant_see_product_in_basket()
         basket_page.should_be_see_empty_message_in_basket()
 
@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.button_basket_click()
        basket_page=BasketPage(browser, browser.current_url)
        basket_page.should_be_see_empty_message_in_basket()
    def test_guest_cant_see_success_message(self,browser):
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.button_basket_click()
        basket_page=BasketPage(browser, browser.current_url)
        basket_page.should_be_cant_see_product_in_basket()
    def test_guest_can_go_to_login_page(self,browser):
      # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        price_book=page.return_price_main()
        name_book=page.return_name_book()
        page.go_to_product_page_user()
        time.sleep(5)
        page.should_be_see_name_add_basket(name_book)
        page.should_be_equil_price_backet(price_book)
            
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self,browser, link):
        link=f"{link}"
        print(f"{link}")
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        price_book=page.return_price_main()
        name_book=page.return_name_book()
        page.go_to_product_page()
        time.sleep(2)
        page.should_be_see_name_add_basket(name_book)
        page.should_be_equil_price_backet(price_book)
    def test_guest_should_see_login_link_on_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link() 
    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page_tr()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # Ё­ЁжЁ «Ё§ЁагҐ¬ Page Object, ЇҐаҐ¤ Ґ¬ ў Є®­бвагЄв®а нЄ§Ґ¬Ї«па ¤а ©ўҐа  Ё url  ¤аҐб 
        page.open()
        page.go_to_product_page_user()
        page.should_cant_see_success_message()
    def test_guest_cant_see_success_message(self,browser): 
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # Ё­ЁжЁ «Ё§ЁагҐ¬ Page Object, ЇҐаҐ¤ Ґ¬ ў Є®­бвагЄв®а нЄ§Ґ¬Ї«па ¤а ©ўҐа  Ё url  ¤аҐб 
        page.open()
        page.should_cant_see_success_message()
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self,browser):
        #link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # Ё­ЁжЁ «Ё§ЁагҐ¬ Page Object, ЇҐаҐ¤ Ґ¬ ў Є®­бвагЄв®а нЄ§Ґ¬Ї«па ¤а ©ўҐа  Ё url  ¤аҐб 
        page.open()
        page.go_to_product_page_user()
        page.should_message_disappeared()
