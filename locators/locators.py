from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLocators:

    # LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']") #кнопка "Вход и регистрация"
    BUTTON_LOGIN_REGESTRATION = (By.XPATH, "//button[text()='Вход и регистрация']") #кнопка "Вход и регистрация"
    BUTTON_NEW_ORDER = (By.XPATH, "//button[text()='Разместить объявление']") #кнопка "Разместить объявление"
    
    FORM_LOGIN = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")

    EMAIL =(By.XPATH, "//input[@placeholder='Введите Email']") #поле для ввода почты
    PASSWORD = (By.XPATH, "//input[@placeholder='Пароль']")  #поле для ввода пароля
    REPEAT_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']") #поле для повторного ввода пароля
    BUTTON_NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']") # копка "Нет аккаунта"
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']") # копка "Войти"

    LOGOUT = (By.XPATH, "//button[text()='Выйти']") #кнопка "Выйти"

    BUTTON_NEW_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']") #кнопка создания нового аккаунта

    NAME_USER = (By.CSS_SELECTOR, ".profileText.name") # имя пользователя
    AVATAR = (By.CSS_SELECTOR, '.circleSmall') # аватар пользователя

    RED_BORDER_EMAIL = (By.XPATH, "//div[@class='input_inputError__fLUP9']/input[@placeholder='Введите Email']/parent::div")
    RED_BORDER_PASSWORD = (By.XPATH, "//div[@class='input_inputError__fLUP9']/input[@placeholder='Пароль']/parent::div")
    RED_BORDER_REPEAT_PASSWORD = (By.XPATH, "//div[@class='input_inputError__fLUP9']/input[@placeholder='Повторите пароль']/parent::div")
    TEXT_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")

    FORM_NEED_AUTH = (By.XPATH, "//form[@class='popUp_shell__LuyqR']/div/h1")
    TITLE_NEW_ORDER = (By.XPATH, "//h1[@class='hi createListing_title__IFtFs' and text()='Новое объявление']")
    NAME_ORDER = (By.XPATH, "//input[@placeholder='Название']")
    ABOUT_ORDER = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE_ORDER = (By.XPATH, "//input[@placeholder='Стоимость']")
    OPEN_CATEGORY = (By.XPATH, "//input[@name='category']/parent::div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    HOBBY_CATEGORY = (By.XPATH,"//span[text()='Хобби']/parent::button")
    OPEN_CITY = (By.XPATH, "//input[@name='city']/parent::div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    SANKT_PETERBURG = (By.XPATH,"//span[text()='Санкт-Петербург']/parent::button")
    TYPE_OLD = (By.XPATH, "//label[text()='Б/У']/parent::div/div")
    BUTTON_POST_ORDER = (By.XPATH, "//button[text()='Опубликовать']")
    FORM_ALL_ORDER = (By.CSS_SELECTOR, ".homePage_homepageStyle__WP-Y1")
    FORM_MY_ORDER = (By.XPATH,"//h1[text()='Мои объявления']/parent::div")

    NAME_LAST_MY_ORDER = (By.XPATH, "//div[@class='profilePage_gridAndPaginaton__togPs']/div/div[1]//div[@class='about']/h2")
    CITY_LAST_MY_ORDER = (By.XPATH, "//div[@class='profilePage_gridAndPaginaton__togPs']/div/div[1]//div[@class='about']/h3")
    PRICE_LAST_MY_ORDER = (By.XPATH, "//div[@class='profilePage_gridAndPaginaton__togPs']/div/div[1]//div[@class='price']/h2")

    MY_ORDERS = (By.XPATH, "//div[@class='profilePage_gridAndPaginaton__togPs']/div")