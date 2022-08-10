from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    MINI_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_forma')
    FIELD_REGISTR = (By.ID, 'id_registration-email')
    FIELD_PASS1 = (By.ID, 'id_registration-password1')
    FIELD_PASS2 = (By.ID, 'id_registration-password2')
    BUTTON_SUBMIT = (By.NAME, 'registration_submit')    
    
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    PRISE_PRODUCT = (By.CSS_SELECTOR, '.product_main > p')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    IN_BASKET_PRISE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > .alertinner > p > strong')
    IN_BASKET_PRODUCT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_FULL = (By.CSS_SELECTOR, '#content_inner > h2')
