from .pages.product_page import ProductPage
import time

def test_guest_can_go_to_login_page(browser):
   # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # �������������� Page Object, �������� � ����������� ��������� �������� � url ����� 
    page.open()
    price_book=page.return_price_main()
    name_book=page.return_name_book()
    page.go_to_product_page()
    time.sleep(10)
    page.should_be_see_name_add_basket(name_book)
    page.should_be_equil_price_backet(price_book)

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # ���� ���������� �����
    link=f"{link}"
    print(f"{link}")
    page = ProductPage(browser, link)   # �������������� Page Object, �������� � ����������� ��������� �������� � url ����� 
    page.open()
    price_book=page.return_price_main()
    name_book=page.return_name_book()
    page.go_to_product_page()
    time.sleep(5)
    page.should_be_see_name_add_basket(name_book)
    page.should_be_equil_price_backet(price_book)
    

    

