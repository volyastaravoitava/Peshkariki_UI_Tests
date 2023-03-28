from selenium.webdriver.common.by import By


class OrderDeliveryPageLocators:
    PRODUCTS_AND_DOCUMENTS_DELIVERY_BTN = (By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/a[1]')
    BUY_PRODUCT_BTN = (By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/a[2]')
    PLACE_ORDER_BTN = (By.XPATH, '//*[@id="aside"]/div/div[2]/div[2]/div[2]/button')
    SHOP_ADDRESS_INPUT = (By.ID, 'address-lfobw135ofyz3w99c1')