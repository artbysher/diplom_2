import random

from faker import Faker

fake = Faker()

def generate_user_body():
    return {
        "email": str(fake.email()),
        "password": str(fake.random_int(min=1000, max=9999)),
        "name": str(fake.first_name())
        }



def generate_order_body():
    ingr_hash = ["61c0c5a71d1f82001bdaaa78",  # "Кристаллы марсианских альфа-сахаридов",
                 "61c0c5a71d1f82001bdaaa7a",  # "Сыр с астероидной плесенью",
                 "61c0c5a71d1f82001bdaaa79",  # "Мини-салат Экзо-Плантаго" ,
                 "61c0c5a71d1f82001bdaaa77",  # "Плоды Фалленианского дерева" ,
                 "61c0c5a71d1f82001bdaaa77",  # "Плоды Фалленианского дерева" ,
                 "61c0c5a71d1f82001bdaaa75",  # "Соус с шипами Антарианского плоскоходца",
                 "61c0c5a71d1f82001bdaaa6d",  # "Флюоресцентная булка R2-D3",
                 "61c0c5a71d1f82001bdaaa6f",  # "Мясо бессмертных моллюсков Protostomia",
                 "61c0c5a71d1f82001bdaaa6c",  # "Краторная булка N-200i"
                 "61c0c5a71d1f82001bdaaa74",  # "Соус традиционный галактический"
                 "61c0c5a71d1f82001bdaaa73",  # "Соус фирменный Space Sauce",
                 "61c0c5a71d1f82001bdaaa6e",  # "Филе Люминесцентного тетраодонтимформа"
                 "61c0c5a71d1f82001bdaaa72",  # "Соус Spicy-X"
                 "61c0c5a71d1f82001bdaaa71",  # "Биокотлета из марсианской Магнолии",
                 "61c0c5a71d1f82001bdaaa70"  # "Говяжий метеорит (отбивная)"
                 ]
    return { "ingredients":random.sample(ingr_hash,3)}

