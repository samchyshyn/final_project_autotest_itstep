from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGUP = (By.XPATH, '//div[@class="top_bar_user"]/a[@href="user/login"]')
    DETAILS = (By.XPATH, '//a[text() = "Детали сотрудничества"]')
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
    LOGO_HEADER = (By.XPATH, '//div[@class="logo logo-desk"]')
    XITY = (By.XPATH, '//span[text()="Хиты"]')
    SKIDKY = (By.XPATH, '//span[text()="Скидки"]')
    NEW_ITEMS = (By.XPATH, '//span[text()="Новинки"]')
    SAMSUNG_CAT = (By.XPATH, '//div[text()="Samsung"]')
    SAMSUNG_J701 = (By.XPATH, '//a[text()="Samsung J701"]')
    SUBSCRIBE = (By.XPATH, '//button[text()="Подписаться!"]')
    INPUT_SUBSCRIBE = (By.XPATH, '//input[@name="submail"]')
    LOGO_FOOTER = (By.XPATH, '//img[@src="images/logo-footer.png"]')

class MainPageLocators:
    TEXT_VOZVRAT = (By.XPATH, '//div[@class="characteristics"]//div[text()="Возврат средств"]')
    TEXT_DOSTAVKA = (By.XPATH, '//div[@class="characteristics"]//div[text()="Бесплатная доставка"]')
    TEXT_OTSTRO4KA = (By.XPATH, '//div[@class="characteristics"]//div[text()="Отсрочка оплаты"]')
    TEXT_TEXPODDERJKA = (By.XPATH, '//div[@class="characteristics"]//div[text()="Тех.поддержка"]')
    BUTTON_NEW_SEE_ALL = (By.XPATH, '//div[@class="new_arrivals"]//a[text()="Показать все"]')
    BUTTON_NEW_SEE_PREV = (By.XPATH, '//div[@class="arrivals_nav arrivals_prev"]')
    BUTTON_NEW_SEE_NEXT = (By.XPATH, '//div[@class="arrivals_nav arrivals_next"]')
    OBLAST_NOVYE_POSTUPLENIJA = (By.XPATH, '//div[@class="col-lg-12"]')
    NEW_PRODYKT = (By.XPATH, '//div[@class="product_panel panel active"]//div[@class="slick-list draggable"]/div/div[3]/div[2]')
    BUTTON_HITS_SEE_ALL = (By.XPATH, '//div[@class="best_nav_container"]/a[text()="Показать все"]')
    BUTTON_HITS_SEE_PREV = (By.XPATH, '//div[@class="best_prev best_nav"]')
    BUTTON_HITS_SEE_NEXT = (By.XPATH, '//div[@class="best_next best_nav"]')
    OBLAST_HITS = (By.XPATH, '//div[@class="bestsellers_panel panel active"]')

    BUTTON_TRENDS_PREV = (By.XPATH, '//div[@class="trends_prev trends_nav slick-arrow"]')
    BUTTON_TRENDS_NEXT = (By.XPATH, '//div[@class="trends_next trends_nav slick-arrow"]')



