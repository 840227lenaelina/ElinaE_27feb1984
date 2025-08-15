from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Дополнительные локаторы
    MODAL_WINDOW = (By.CLASS_NAME, 'swal2-header')  # Модальное окно
    MODAL_BUTTON = (By.CLASS_NAME, 'swal2-close')  # Закрытие модального окна

    def is_product_displayed(self):
        try:
            product_image = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "basket__img-box"))
            )
            return product_image.is_displayed()
        except Exception:
            return False

    def delete_product(self):
        # Ожидаем загрузки элемента кнопки удаления из корзины
        delete_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.basket__delete.js-item-delete > button"))
        )
        delete_button.click()

    def is_product_deleted(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "basket__img-box"))
            )
            return True
        except Exception:
            return False

    def is_element_visible(self, locator):
        """Проверяет, видим ли элемент с заданным локатором."""
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True if element else False
        except Exception:
            return False

    def click(self, locator):
        """Кликает на элемент с заданным локатором."""
        try:
            element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Error clicking on element: {e}")

    def is_modal_displayed(self):
        """Проверяет, отображается ли модальное окно."""
        return self.is_element_visible(self.MODAL_WINDOW)

    def close_modal_if_open(self):
        """Закрывает модальное окно, если оно открыто."""
        if self.is_modal_displayed():
            self.click(self.MODAL_BUTTON)
            