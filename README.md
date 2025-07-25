## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Александра Шеремет

## <h>Когорта: #17</h>
<hr>

## <h>Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results

 
### Реализованные сценарии

Созданы API-тесты, покрывающие сценарии: `Создание пользователя`, `Авторизация пользователя`, `Изменение данных пользователя`, `Создание заказа`, `Получение заказов конкретного пользователя`


### Структура проекта

- `methods` - пакет, содержащий методы для тестов
- `tests` - пакет, содержащий тесты, разделенные по классам. `test_bun.py`, `test_burger.py`, `test_database.py`, `test_ingredient.py`
- `allure-results` - пакет, содержащий allure отчет
- `data.py` - фаил с URL и текстами ошибок
- `generators.py` - фаил с Faker и рандомайзером данных для тестов

<hr>
