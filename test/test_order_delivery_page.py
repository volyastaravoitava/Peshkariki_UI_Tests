import time
import pytest
from pages.order_delivery_page import OrderDeliveryPage


def test_obligatory_fields_empty(browser):
        """Проверка отображения обязательных для заполнения полей ввода при невведенных в поля ввода данных"""
        link = 'https://peshkariki.ru/orderDelivery'
        page = OrderDeliveryPage(browser, link)
        page.open()
        page.select_products_and_documents_delivery()
        time.sleep(3)
        page.place_order_btn()
        time.sleep(3)
        browser.save_screenshot('result_test_obligatory_fields_empty.png')

