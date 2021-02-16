# Установка

Установить зависимости `pip install -r requirements.txt`

Подключение к БД осуществляется в файле `database.py`

По желанию запустить скрипт для добавления тестовых записей `python init.py`

# Запуск

Запустить сервер `python app.py`

# Струкрура

Модель Auto состоит из следующих полей:

- _id
- vendor
- model_name
- year_issue
- color
- vin_code

# Роуты:
GET - `/auto` - Получение всех записей

GET - `/auto?color=Green` - Фильтрация записей по определенному полю

GET - `/auto/view?id=602c1e9a72432451c5f24738` - Получение определенной записи

PUT - `/auto/create?vendor=Tesla&model_name=Test&color=Yellow&year_issue=2020` - Создание новой записи

POST - `/auto/update?id=602c0a28f15e4342e220e8e8&color=White` - Обновление существующей записи

DELETE - `/auto/delete?id=602c0a28f15e4342e220e8e8` - Обновление существующей записи

--------------

Старался сделать быстро так как есть еще много заданий, поэтому код немного неструктурирован. Надеюсь это не будет большой проблемой.