import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By

link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.skip
@pytest.mark.parametrize('post', [*range(0, 7), pytest.param(7, marks=pytest.mark.xfail(reason='some bug')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, post):
   link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{post}'
   page = ProductPage(browser, link)
   page.open()
   page.click_button_add_to_cart()
   page.solve_quiz_and_get_code()
   page.should_be_added_to_cart()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
   page = ProductPage(browser, link)
   page.open()
   page.click_button_add_to_cart()
   page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
   page = ProductPage(browser, link)
   page.open()
   page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
   page = ProductPage(browser, link)
   page.open() 
   page.click_button_add_to_cart()
   page.should_dissapear_of_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
   link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
   page = ProductPage(browser, link)
   page.open()
   page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
   link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
   page = ProductPage(browser, link)
   page.open()
   page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
   link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
   page = BasketPage(browser, link)
   page.open()
   page.go_to_mini_basket()
   page.is_basket_not_empty()   
   page.is_basket_empty()
