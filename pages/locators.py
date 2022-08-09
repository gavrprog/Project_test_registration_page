from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_forma')
    
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    PRISE_PRODUCT = (By.CSS_SELECTOR, '.product_main > p')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    IN_BASKET_PRISE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > .alertinner > p > strong')
    IN_BASKET_PRODUCT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > .alertinner > strong')