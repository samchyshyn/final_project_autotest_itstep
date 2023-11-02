from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGUP = (By.XPATH, '//div[@class="top_bar_user"]/a[@href="user/login"]')
    FEEDBACK = (By.XPATH, '//a[text()="Обратная связь"]')
    DELIVERY = (By.XPATH, '//a[text()="Доставка"]')
    WARRANTY = (By.XPATH, '//a[text()="Гарантия"]')
    PHONE = (By.XPATH, '//*[text()="+38 098 911 95 22"]')
    CURRENCY = (By.XPATH, '//select[@id ="currency"]')

    VALUTA_UAN = (By.XPATH, '//option[@class="custom_list clc"]')
    VALUTA_USD = (By.XPATH, '//option[@value="USD"]')
    VALUTA_EUR = (By.XPATH, '//option[@value="EUR"]')
    BASKET = (By.XPATH, '//a[@href="cart/show"]')
    WISH = (By.XPATH, '//a[@href="wish/show"]')
    INPUT_SEARCH = (By.XPATH, '//input[@class="header_search_input tt-hint"]')
    BUTTON_SEARCH = (By.XPATH, '//button[@class="header_search_button trans_300"]')
    LOGO_CASENIK = (By.XPATH, '//div[@class="logo logo-desk"]')
    XITY = (By.XPATH, '//span[text()="Хиты"]')
    SKIDKY = (By.XPATH, '//span[text()="Скидки"]')
    NEW_ITEMS = (By.XPATH, '//span[text()="Новинки"]')
    SAMSUNG_CAT = (By.XPATH, '//div[text()="Samsung"]')
    SAMSUNG_J701 = (By.XPATH, '//a[text()="Samsung J701"]')
    SUBSCRIBE = (By.XPATH, '//button[text()="Подписаться!"]')
    INPUT_SUBSCRIBE = (By.XPATH, '//input[@name="submail"]')
    LOGO_FOOTER = (By.XPATH, '//img[@src="images/logo-footer.png"]')


