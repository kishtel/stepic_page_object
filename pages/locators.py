from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.ID,"login_form")
    LOOGIN_REGISTER_FORM=(By.ID,"register_form")
class ProductPageLocators():
    BUTTON_SUBMIT= (By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")
    BUTTON_REVIEW=(By.ID,"write_review")
    BUTTON_WISH=(By.CSS_SELECTOR,"btn.btn-lg.btn-wishlist")
    PRODUCT_FORM=(By.ID,"add_to_basket_form")
    PRODUCT_PRICE_BACKET=(By.XPATH,"//div[@class='alertinner ']/p[1]/strong")
    PRODUCT_PRICE_MAIN=(By.CSS_SELECTOR,".product_main .price_color")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main h1")
    PRODUCT_NAME_BACKET=(By.XPATH,"//div[@id='messages']/div[contains(@class,'alert-success')][1]/div/strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alertinner")
