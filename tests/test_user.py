import allure

import data
from generators import generate_user_body
from methods.user_methods import UsersMethods


class TestCreateUser:

    @allure.title('Тест на успешное создание пользователя')
    @allure.description('Создаем пользователя и проверяем запрос возвращает правильный код ответа 200 и содержит {"success":true}')
    def test_success_create_user(self, generate_user_data):
        user = UsersMethods.create_user(generate_user_data[0])
        assert user.status_code == 200 and user.json().get("success") is True

    @allure.title('Тест на получение ошибки при попытке создании двух одинаковых пользователей')
    @allure.description('Создаем последовательно двух пользователей передавая одинаковые данные емайл, пароль, имя и проверяем что возвращается ошибка')
    def test_create_duplicate_user(self, generate_user_data):
        user1 = UsersMethods.create_user(generate_user_data[0])
        user2 = UsersMethods.create_user(generate_user_data[0])
        assert user1.status_code == 200 and user2.status_code == 403 and user2.json().get("message") == data.Return.DUPLICATE_USER

    @allure.title('Тест на получение ошибки при попытке создания пользователя без email')
    @allure.description('Пытаемся создать пользователя передавая тело без email и проверяем, что возвращается ошибка')
    def test_create_user_without_email(self):
        user_body = generate_user_body()
        user_body.pop("email")
        user = UsersMethods.create_user(user_body)

        assert user.status_code == 403 and user.json().get(
            "message") == data.Return.NO_REQUIRED_DATA

    @allure.title('Тест на получение ошибки при попытке создания пользователя без пароля')
    @allure.description(
        'Пытаемся создать пользователя передавая тело без пароля и проверяем, что возвращается ошибка и сообщение Недостаточно данных для создания учетной записи')
    def test_create_user_without_password(self):
        user_body = generate_user_body()
        user_body.pop("password")
        user = UsersMethods.create_user(user_body)

        assert user.status_code == 403 and user.json().get(
            "message") == data.Return.NO_REQUIRED_DATA