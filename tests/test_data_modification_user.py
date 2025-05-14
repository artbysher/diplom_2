import allure
import pytest
from faker import Faker
import data

from methods.user_methods import UsersMethods

fake = Faker()

class TestDataModificationUser:

    @allure.title('Тест на успешное изменение данных авторизованного пользователя')
    @allure.description('Создаем пользователя и проверяем что пользователь может изменить свои данные после авторизации,код 200 и изменилось поле email' )

    @pytest.mark.parametrize("field, new_value", [
        ("email", str(fake.email())),
        ("password", str(fake.random_int(min=1000, max=9999))),
        ("name", "NewName")
    ])
    def test_update_user_field(self, generate_user_data, field, new_value):
        UsersMethods.create_user(generate_user_data[0])
        access_token = UsersMethods.get_user_accessToken(generate_user_data[1], generate_user_data[2])
        new_body = generate_user_data[0].copy()
        new_body[field] = new_value
        new_date_user = UsersMethods.update_user(new_body, access_token)
        assert new_date_user.status_code == 200 and new_date_user.json().get(
            "success") == True
        UsersMethods.update_user(generate_user_data[0], access_token)


    @allure.title('Тест на ошибку при изменении данных без авторизации')
    @allure.description('Создаем пользователя и проверяем что получаем ошибку при попытке изменить данные без авторизации,код' )
    @pytest.mark.parametrize("field, new_value", [
        ("email", str(fake.email())),
        ("password", str(fake.random_int(min=1000, max=9999))),
        ("name", "NewName")
    ])
    def test_update_user_field_without_auth(self, generate_user_data, field, new_value):
            UsersMethods.create_user(generate_user_data[0])
            new_body = generate_user_data[0].copy()
            new_body[field] = new_value
            new_date_user = UsersMethods.update_user(new_body, None)
            assert (new_date_user.status_code == 401 and  new_date_user.json()['success'] is False
                and new_date_user.json().get("message") == data.Return.UNAUTHORIZED)

