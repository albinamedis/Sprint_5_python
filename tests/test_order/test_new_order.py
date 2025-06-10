from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import TestLocators
from tests.data import email_reg, password, name_order, about_order, price_order

class TestOrder:

    def test_new_order_not_auth(self, driver):
        driver.find_element(*TestLocators.BUTTON_NEW_ORDER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_NEED_AUTH)))
        form = driver.find_element(*TestLocators.FORM_NEED_AUTH)
        text_form = form.text

        assert text_form == 'Чтобы разместить объявление, авторизуйтесь'

    
    def test_new_order_auth(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))

        driver.find_element(*TestLocators.EMAIL).send_keys(email_reg)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGOUT)))

        driver.find_element(*TestLocators.BUTTON_NEW_ORDER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.TITLE_NEW_ORDER)))
        
        driver.find_element(*TestLocators.NAME_ORDER).send_keys(name_order)
        driver.find_element(*TestLocators.ABOUT_ORDER).send_keys(about_order)
        driver.find_element(*TestLocators.PRICE_ORDER).send_keys(price_order)
        driver.find_element(*TestLocators.OPEN_CATEGORY).click()
        driver.find_element(*TestLocators.HOBBY_CATEGORY).click()
        driver.find_element(*TestLocators.OPEN_CITY).click()
        driver.find_element(*TestLocators.SANKT_PETERBURG).click()
        driver.find_element(*TestLocators.TYPE_OLD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.TYPE_OLD)))
        driver.find_element(*TestLocators.BUTTON_POST_ORDER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_ALL_ORDER)))
        driver.find_element(*TestLocators.AVATAR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_MY_ORDER)))
        element = driver.find_element(*TestLocators.FORM_MY_ORDER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_LAST_MY_ORDER)))
        name_last_my_order = driver.find_element(*TestLocators.NAME_LAST_MY_ORDER).text
        city_last_my_order = driver.find_element(*TestLocators.CITY_LAST_MY_ORDER).text
        price_last_my_order = driver.find_element(*TestLocators.PRICE_LAST_MY_ORDER).text

        assert name_last_my_order == name_order and city_last_my_order == "Санкт-Петербург" and price_last_my_order == '10 000 ₽'
        