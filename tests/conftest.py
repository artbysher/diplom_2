import pytest

from generators import generate_user_body
from methods.user_methods import UsersMethods


@pytest.fixture
def generate_user_data():
    user_body = generate_user_body()
    email = user_body['email']
    password = user_body['password']
    yield [user_body, email, password]
    access_token = UsersMethods.get_user_accessToken( email, password)
    UsersMethods.delete_user(access_token)

