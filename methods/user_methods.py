import requests
import data


class UsersMethods:
    @staticmethod
    def create_user(body):
        return requests.post(data.Url.CREATE_USER_URL, json=body)

    @staticmethod
    def login_user( email, password):
        email_password = {'email': email, 'password':  password }
        return requests.post(data.Url.LOGIN_USER_URL, json=email_password)

    @staticmethod
    def delete_user(access_token):
        return requests.delete(data.Url.USER_URL, headers={ "Authorization": access_token })

    @staticmethod
    def get_user_accessToken( email, password):
        email_password = {'email': email, 'password':  password }
        responce = requests.post(data.Url.LOGIN_USER_URL, json=email_password)
        if responce.status_code == 200:
            return responce.json()['accessToken']

    @staticmethod
    def update_user(body, access_token):
        return requests.patch(data.Url.USER_URL, headers={"Authorization": access_token}, json=body)

    @staticmethod
    def get_user_info(access_token):
        return requests.get(data.Url.USER_URL, headers={"Authorization": access_token})
