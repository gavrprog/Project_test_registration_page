from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def is_basket_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FULL), "Basket is empty, but should be with product"
        
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket full, but should not be"