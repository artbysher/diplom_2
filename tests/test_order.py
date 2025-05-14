import allure
import pytest

import data
import generators

from methods.order_methods import OrdersMethods
from methods.user_methods import UsersMethods


class TestCreateOrder:

    @allure.title('Тест на успешное создание заказа авторизованным пользователем')
    @allure.description('Создаем пользователя, берем его токен и проверяем запрос на создание заказа код ответа 200 и содержит {"success":true}')
    def test_create_order_with_auth(self, generate_user_data):
        UsersMethods.create_user(generate_user_data[0])
        access_token = UsersMethods.get_user_accessToken(generate_user_data[1], generate_user_data[2])
        body = generators.generate_order_body()
        order = OrdersMethods.create_order(access_token, body)
        assert order.status_code == 200 and order.json().get("success") is True

    @allure.title('Тест на  создание заказа не авторизованным пользователем')
    @allure.description(
        'Проверяем запрос на создание заказа без токена код ответа 200 и содержит {"success":true}')
    def test_create_order_without_auth(self):
        body = generators.generate_order_body()
        order = OrdersMethods.create_order(None,body)
        assert order.status_code == 200 and order.json().get("success") is True

    @allure.title('Тест на получение ошибки при создании заказа без ингредиентов')
    @allure.description('Создаем пользователя, берем его токен и проверяем запрос на создание заказа без ингредиентов, код ответа 400 и содержит {"success":false}')
    def test_create_order_without_ingredients(self, generate_user_data):
        UsersMethods.create_user(generate_user_data[0])
        access_token = UsersMethods.get_user_accessToken(generate_user_data[1], generate_user_data[2])
        body = {"ingredients": []}
        order = OrdersMethods.create_order(access_token, body)
        assert order.status_code == 400 and order.json().get("success") is False
        assert order.json().get("message") == data.Return.NO_INGREDIENT

    @allure.title('Тест на получение ошибки при создании заказа c невалидными хеш ингридиентов')
    @allure.description(
        'Проверяет, что при неверных хешах ингредиентов API возвращает код 500.')
    @pytest.mark.parametrize('invalid_hash', ["61r0cdfghytf82001bdaaa20", '0000000', 'Spicy'])
    def test_create_order_invalid_ingredients(self, generate_user_data,invalid_hash ):
        UsersMethods.create_user(generate_user_data[0])
        access_token = UsersMethods.get_user_accessToken(generate_user_data[1], generate_user_data[2])
        body = {"ingredients": [invalid_hash]}
        order = OrdersMethods.create_order(access_token, body)
        assert order.status_code == 500

    @allure.title('Тест на получение списка заказов авторизованного пользователя')
    @allure.description(
        'Создаем пользователя и заказ код ответа 200 и содержит {"success":true}')
    def test_create_order_with_auth(self, generate_user_data):
        UsersMethods.create_user(generate_user_data[0])
        access_token = UsersMethods.get_user_accessToken(generate_user_data[1], generate_user_data[2])
        OrdersMethods.create_order(access_token, generators.generate_order_body())
        list_user_orders = OrdersMethods.get_user_orders(access_token)
        assert list_user_orders.status_code == 200 and list_user_orders.json().get("success") is True and  isinstance(list_user_orders.json()["orders"], list)

    @allure.title('Тест на получение ошибки при получения заказов без авторизации')
    @allure.description(
        'Проверяется, что сервер возвращает 401 и сообщение об ошибке.')
    def test_create_order_with_auth(self):

        list_user_orders = OrdersMethods.get_user_orders(None)
        assert list_user_orders.status_code == 401 and list_user_orders.json().get("success") is False
        assert list_user_orders.json().get("message") == data.Return.UNAUTHORIZED