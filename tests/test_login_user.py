import allure

import data
from generators import generate_user_body
from methods.user_methods import UsersMethods


class TestLoginUser:

    @allure.title('Тест на успешную авторизацию пользователя')
    @allure.description('Создаем пользователя и проверяем что с этими логином и паролем пользователь может авторизоваться, код 200 и в теле ответа присутсвует "accessToken"')
    def test_auth_user(self, generate_user_data):
        UsersMethods.create_user(generate_user_data[0])
        user_login =UsersMethods.login_user(generate_user_data[1],generate_user_data[2])

        assert user_login.status_code == 200 and user_login.json()["accessToken"].startswith("Bearer")


    @allure.title('Тест на ошибку при  авторизации под несуществующим пользователем')
    @allure.description(
        'Вводим логин и пароль несуществующего пользователя и проверяем что получаем ошибку 401 и сообщение ' )
    def test_auth_with_invalid_user(self):
        user_body = generate_user_body()
        email = user_body['email']
        password = user_body['password']
        user_login = UsersMethods.login_user(email,password)

        assert (user_login.status_code == 401
                and user_login.json().get("message") == data.Return.INCORRECT_DATA_AUTH)


