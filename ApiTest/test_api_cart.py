import requests
import pytest
import allure
from urllib.parse import urlencode
from settings import *

@pytest.fixture(scope="session")
def base_url():
    return api_base_url

class TestAPI:
    def setup_class(self):
        self.session = requests.Session()

    @pytest.mark.api
    @allure.title("Тест добавляет товар в корзину")
    @allure.description("Проверяет статус-код и наличие товара в корзине.")
    def test_add_to_cart(self, base_url):
        with allure.step("Подготовка данных"):
            data = {
                'product_id': product_id,
                'LANG_key': 'ru',
                'S_wh': '1',
                'S_CID': S_CID,
                'S_cur_code': 'rub',
                'S_koef': '1',
                'quantity': '1',
                'S_hint_code': '',
                'S_customerID': ''
            }

            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            full_url = f"{base_url}add_products_to_cart_from_preview.php"

        with allure.step("Отправка POST-запроса"):
            response = self.session.post(full_url, data=urlencode(data), headers=headers)

        with allure.step("Проверка статуса ответа"):
            print("Response Code:", response.status_code) 
            print("Response Body:", response.text) 
            assert response.status_code == 200, f"Ошибка добавления товара: {response.text}"

    @pytest.mark.api
    @allure.title("Тест удаляет товар из корзины")
    @allure.description("Проверяет статус-код и отсутствие товара в корзине.")
    def test_delete_to_cart(self, base_url):
        with allure.step("Подготовка данных"):
            data = {
                'product_id': product_id,
                'LANG_key': 'ru',
                'S_wh': '1',
                'S_CID': S_CID,
                'S_cur_code': 'rub',
                'S_koef': '1',
                'quantity': '1',
                'S_hint_code': '',
                'S_customerID': ''
            }

            encoded_body = urlencode(data)

            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

            full_url = f"{base_url}delete_products_from_cart_preview.php"

        with allure.step("Отправка POST-запроса"):
            response = self.session.post(full_url, data=encoded_body, headers=headers)

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, "Ошибка удаления товара"