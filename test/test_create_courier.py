import allure
import pytest
import requests

from data_helper import post_courier, generate_random_string

@allure.description('Класс тестирования курьера. Создание.')
class TestCreateCourier:

    @allure.step('Создаем всегда разных курьеров заполняя все поля. Ожидаем ответ == 201')
    def test_create_courier_true(self):
        payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
        }
        response = requests.post(post_courier, data=payload)
        assert response.status_code == 201

    @allure.step('Передали существующие данные.')
    def test_cant_create_two_same_courier_false(self):
        payload = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
            }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {"code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."} and response.status_code == 409

    @allure.step('Сгенерировали пароль и имя, логин пустой.')
    def test_missing_login_data_false(self):
        payload = {
            "login": "",
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"} and response.status_code == 400

    @allure.step('Сгенерировали логин и имя, пароль пустой.')
    def test_missing_password_data_false(self):
        payload = {
            "login": generate_random_string(10),
            "password": "",
            "firstName": generate_random_string(10)
        }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"} and response.status_code == 400

    @allure.step('Сгенерировали логин и пароль, имя пустое.')
    def test_missing_fname_data_true(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": ""
        }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {'ok': True} and response.status_code == 201

    @allure.step('Логин существует в системе, пароль и имя сгенерировали.')
    def test_cant_create_two_same_logins_true(self):
        payload = {
            "login": "ninja",
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(post_courier, data=payload)
        assert response.json() == {"code": 409,
                                   "message": "Этот логин уже используется. Попробуйте другой."} and response.status_code == 409
