class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER_URL =  f'{BASE_URL}/api/auth/register'
    LOGIN_USER_URL = f'{BASE_URL}/api/auth/login'
    USER_URL = f'{BASE_URL}/api/auth/user'


    ORDER_URL = f'{BASE_URL}/api/orders'


class Return:
    NO_REQUIRED_DATA = "Email, password and name are required fields"
    DUPLICATE_USER = "User already exists"
    INCORRECT_DATA_AUTH = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"
    FORBIDDEN_USER = "User with such email already exists"
    NO_INGREDIENT =  "Ingredient ids must be provided"

