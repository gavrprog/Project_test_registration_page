import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('post', [*range(0, 7), pytest.param(7, marks=pytest.mark.xfail(reason='some bug')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, post):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{post}'
    page = ProductPage(browser, link)
    page.open()                      
    page.click_button_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_cart()