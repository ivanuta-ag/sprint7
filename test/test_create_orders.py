import json
import allure
import pytest
import requests

from data_helper import generate_random_string, generate_random_numbers, create_order


@allure.description('Проверяем ручки раздела "Заказы (Orders)"')
class TestCreateOrders:

    # делаем параметризацию цвета и даты доставки
    # передаем создание по 1 цвету, без цвета и одновременно 2 цвета
    @pytest.mark.parametrize('change',["BLACK","SILVER","",["BLACK","SILVER"]])
    # передаем 3 разные даты доставки
    @pytest.mark.parametrize('date_order', ["2029-12-01", "2019-12-01", "2026-12-01"])
    @allure.step('Успешное создание заказа заполняя все поля рандомными значениями')
    def test_create_order_true(self, change, date_order):
        payload = {
        "firstName": generate_random_string(10),
        "lastName": generate_random_string(10),
        "address": generate_random_string(10),
        "metroStation": generate_random_numbers(3),
        "phone": generate_random_numbers(11),
        "rentTime": generate_random_numbers(1),
        "deliveryDate": date_order,
        "comment": generate_random_string(10),
        "color": [
            change]
        }
        json_string = json.dumps(payload)
        response = requests.post(create_order, data=json_string)
        assert "track" in response.json() and response.status_code == 201
        assert "BLACK","SILVER" in response.json()

    @allure.step('Проверяем что возвращается список заказов. Лимит заказов для отображения =1, страница=0')
    def test_get_orders(self):
        response = requests.get(f'{create_order}?limit=1&page=0')
        assert "orders" in response.json()
        assert response.status_code==200