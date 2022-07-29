import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

# def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # вызываем метод из BasePage<-MainPage - открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)