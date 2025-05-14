import requests
import data


class OrdersMethods:
    @staticmethod
    def create_order(access_token,body):
        return requests.post(data.Url.ORDER_URL, headers={"Authorization": access_token}, json=body)

    @staticmethod
    def get_user_orders(access_token):
        return requests.get(data.Url.ORDER_URL , headers={"Authorization": access_token} )


