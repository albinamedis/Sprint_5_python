from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import TestLocators
from tests.data import email, password, email_not_mask, expected_rgb,email_reg


class TestRegistartion:

    def test_new_accaunt(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))
        driver.find_element(*TestLocators.BUTTON_NO_ACCOUNT).click()

        driver.find_element(*TestLocators.EMAIL).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REPEAT_PASSWORD).send_keys(password)

        driver.find_element(*TestLocators.BUTTON_NEW_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGOUT)))

        text_name = driver.find_element(*TestLocators.NAME_USER).text
        assert (driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/regiatration') and (text_name == "User.") and (driver.find_elements(*TestLocators.AVATAR))


    def test_new_accaunt_not_mask(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))
        driver.find_element(*TestLocators.BUTTON_NO_ACCOUNT).click()

        driver.find_element(*TestLocators.EMAIL).send_keys(email_not_mask)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_NEW_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.RED_BORDER_EMAIL)))

        element_email = driver.find_element(*TestLocators.RED_BORDER_EMAIL)
        element_passsword = driver.find_element(*TestLocators.RED_BORDER_PASSWORD)
        element_repeat_passsword = driver.find_element(*TestLocators.RED_BORDER_REPEAT_PASSWORD)

        border_value_email = element_email.value_of_css_property('border')
        border_value_passsword = element_passsword.value_of_css_property('border')
        border_value_repeat_passsword = element_repeat_passsword.value_of_css_property('border')
        text_error = driver.find_element(*TestLocators.TEXT_ERROR).text

        assert ((expected_rgb in border_value_email) 
                and (expected_rgb in border_value_passsword) 
                and (expected_rgb in border_value_repeat_passsword) and (text_error=='Ошибка'))
        

    def test_repeat_regestration_email(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))
        driver.find_element(*TestLocators.BUTTON_NO_ACCOUNT).click()

        driver.find_element(*TestLocators.EMAIL).send_keys(email_reg)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_NEW_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.RED_BORDER_EMAIL)))

        element_email = driver.find_element(*TestLocators.RED_BORDER_EMAIL)
        element_passsword = driver.find_element(*TestLocators.RED_BORDER_PASSWORD)
        element_repeat_passsword = driver.find_element(*TestLocators.RED_BORDER_REPEAT_PASSWORD)

        border_value_email = element_email.value_of_css_property('border')
        border_value_passsword = element_passsword.value_of_css_property('border')
        border_value_repeat_passsword = element_repeat_passsword.value_of_css_property('border')
        text_error = driver.find_element(*TestLocators.TEXT_ERROR).text

        assert ((expected_rgb in border_value_email) 
                and (expected_rgb in border_value_passsword) 
                and (expected_rgb in border_value_repeat_passsword) and (text_error=='Ошибка'))

        
    def test_autorisation(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))

        driver.find_element(*TestLocators.EMAIL).send_keys(email_reg)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGOUT)))

        text_name = driver.find_element(*TestLocators.NAME_USER).text
        assert (driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/login') and (text_name == "User.") and (driver.find_element(*TestLocators.AVATAR))


    def test_logout(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.FORM_LOGIN)))

        driver.find_element(*TestLocators.EMAIL).send_keys(email_reg)
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGOUT)))
        driver.find_element(*TestLocators.LOGOUT).click()
        WebDriverWait(driver, 5).until_not(expected_conditions.visibility_of_element_located((TestLocators.NAME_USER)))
        log_and_reg = driver.find_element(*TestLocators.BUTTON_LOGIN_REGESTRATION).text
            
        avatar = driver.find_elements(*TestLocators.AVATAR)
        name = driver.find_elements(*TestLocators.NAME_USER)
        assert (log_and_reg == 'Вход и регистрация') and (len(avatar)==0) and (len(name)==0)

            