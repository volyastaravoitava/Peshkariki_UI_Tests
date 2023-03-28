from pages.base_page import BasePage
from pages.locators import OrderDeliveryPageLocators
from pages.test_data import AddressOptions


class OrderDeliveryPage(BasePage):

    def select_products_and_documents_delivery(self):
        order_type_btn = self.browser.find_element(*OrderDeliveryPageLocators.PRODUCTS_AND_DOCUMENTS_DELIVERY_BTN)
        order_type_btn.click()

    def select_buy_product(self):
        order_type_btn = self.browser.find_element(*OrderDeliveryPageLocators.BUY_PRODUCT_BTN)
        order_type_btn.click()

    def input_shop_address(self):
        shop_address = self.browser.find_element(*OrderDeliveryPageLocators.SHOP_ADDRESS_INPUT)
        shop_address.send_keys(*AddressOptions.VALID_ADDRESS)

    def place_order_btn(self):
        place_order_btn = self.browser.find_element(*OrderDeliveryPageLocators.PLACE_ORDER_BTN)
        place_order_btn.click()





