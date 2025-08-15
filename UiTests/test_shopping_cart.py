import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from product_page import ProductPage
from cart_page import CartPage

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def clear_cart(driver):
    """Функция для очистки корзины перед каждым тестом."""
    driver.get("https://altaivita.ru/cart/")
    cart_page = CartPage(driver)
    if cart_page.is_product_displayed():
        cart_page.delete_product()  # Удаляем продукт, если он в корзине

@allure.feature('Shopping Cart')
@allure.story('Add Product')
def test_add_product(driver):
    clear_cart(driver)  # Очищаем корзину перед тестом
    driver.get("https://altaivita.ru/product/altayskiy-klyuch_promo/")

    product_page = ProductPage(driver)
    product_page.add_product_to_cart()

    driver.get("https://altaivita.ru/cart/")
    cart_page = CartPage(driver)

    assert cart_page.is_product_displayed(), "Product is not displayed in the cart."

@allure.story('Delete Product')
def test_delete_product(driver):
    clear_cart(driver)  # Очищаем корзину перед тестом
    driver.get("https://altaivita.ru/product/altayskiy-klyuch_promo/")

    product_page = ProductPage(driver)

    try:
        product_page.add_product_to_cart()
    except Exception as e:
        pytest.fail(f"Не удалось добавить продукт в корзину: {str(e)}")

    driver.get("https://altaivita.ru/cart/")
    cart_page = CartPage(driver)

    if cart_page.is_modal_displayed():
        cart_page.close_modal_if_open()

    cart_page.delete_product()
    
    assert cart_page.is_product_deleted(), "Product not deleted from the cart."
