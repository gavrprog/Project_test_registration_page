import pytest
from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # вызываем метод из BasePage<-MainPage - открываем страницу
    page.click_button_add_to_cart()  # выполняем метод страницы — жмем кнопку
    page.solve_quiz_and_get_code()
    page.should_be_added_to_cart()