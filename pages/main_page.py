from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedbback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button DELIVERY is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button WARRANTY is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_number_telefon(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element number telefonu not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_CURRENCY(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Element CURRENCY not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_UAN(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.VALUTA_UAN), \
            " The Element UAN is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_EUR(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.VALUTA_EUR), \
            " The Element EUR is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_USD(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.VALUTA_USD ), \
            " The Element USD is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.INPUT_SEARCH), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SEARCH), \
            "The search button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_wish_button(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hity_button(self):
        assert self.is_element_present(*locators.BasePageLocators.HITY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_skidki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SKIDKY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_novinki_button(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW_ITEMS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_category(self):
        assert self.is_element_present(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.HEAD_CAT_SAMSUNG), \
            "The element is not present"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_slider(self):
        assert  self.is_element_present(*locators.MainPageLocators.SCREEN_SLIDER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_zaradky(self):
        assert  self.is_element_present(*locators.MainPageLocators.MAIN_CAT_ZARADKY)
        "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_subcat(self):
        assert self.hover_action(*locators.MainPageLocators.MAIN_CAT_ZARADKY), \
            "Element 'main category' is not present"
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SUBCAT), \
            "Element 'main subcategory' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_VOZVRAT_SREDSTV), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_delivery(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_DOSTAVKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_otsrochka(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_OTSROCHKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_support(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_SUPPORT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEW_SEE_ALL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_prev_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEW_SEE_PREV), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_next_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEW_SEE_NEXT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.OBLAST_NOVYE_POSTUPLENIJA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_product_8(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_PRODUCT_8), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_SHOW_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE_BUTTON), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert  self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
            "The element footer logo is not present"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE_BUTTON), \
            "Element 'SUBSCRIBE' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success_after_subscribe(self):
        assert self.is_elements_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")



