import allure
import pytest
import requests

from data_helper import post_courier, generate_random_string, login_courier

@allure.description('Проверяем ручку "Логин курьера в системе"')
class TestCheckLoginCourier:

    @allure.step('Создаем и регистрируем всегда разных курьеров, и пробуем зайти в систему под его логином и паролем. Ожидаем успех == 200')
    def test_login_courier_true(self):
        payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10)
        }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {'ok': True} and response.status_code == 201
        id_courier = payload
        response = requests.post(login_courier, id_courier)
        assert response.status_code == 200

    @allure.step('Генерируем логин и пароль и пробуем зайти в систему.')
    def test_login_noreg_courier_true(self):
        payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10)
        }
        response = requests.post(login_courier, payload)
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"} and response.status_code == 404

    @allure.step('Попытались зайти без пароля.')
    def test_login_noreg_nopass_courier_true(self):
        payload = {
        "login": generate_random_string(10),
        "password": ""
        }
        response = requests.post(login_courier, payload)
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"} and response.status_code == 400

