from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        # Добавляем куки
        self.driver.add_cookie({
            'name': 'cookie_consent',
            'value': 'accepted',
            'path': '/',
            'domain': 'altaivita.ru',
            'secure': False
        })
        self.driver.refresh()  # Обновляем страницу, чтобы куки применились

        # Ожидаем загрузки элемента кнопки добавления в корзину
        add_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'main-btn') and contains(@class, 'blue')]"))
        )
        add_button.click()
