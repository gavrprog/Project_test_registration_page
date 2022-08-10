from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

   def click_button_add_to_cart(self):
      self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

   def should_be_added_to_cart(self):
      self.is_product_in_cart_equal()
      self.is_prise_in_cart_equal()

   def is_product_in_cart_equal(self):
      product_in_description = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
      product_in_cart = self.browser.find_element(*ProductPageLocators.IN_BASKET_PRODUCT).text
      assert product_in_description == product_in_cart, f"Product in the cart ({product_in_cart}) is not equal to choosed product ({product_in_description})"

   def is_prise_in_cart_equal(self):
      prise_in_description = self.browser.find_element(*ProductPageLocators.PRISE_PRODUCT).text
      prise_in_cart = self.browser.find_element(*ProductPageLocators.IN_BASKET_PRISE).text
      assert prise_in_description == prise_in_cart, f"Product in the cart ({prise_in_cart}) is not equal to choosed product ({prise_in_description})"
      
   def should_not_be_success_message(self):
      assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

   def should_dissapear_of_success_message(self):
      assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissapear, but should be"