from bson import ObjectId

import database
import exceptions
from auto import Auto

# Define auto collection
collection_name = 'cars'
auto_collection = database.db[collection_name]


def get_all(params):
    """
    Get all cars
    :param params:
    :return:
    """
    autos = database.find_document(auto_collection, params, True)

    result = []
    for auto in autos:
        auto_obj = Auto()
        auto_obj.load_json(auto)
        result.append(auto_obj.serialize())

    return result


def get_one(id_):
    """
    Get one car
    :param id_:
    :return:
    """
    db_data = database.find_document(auto_collection, {'_id': ObjectId(id_)})
    if not db_data:
        raise exceptions.NotFound("Object not found")

    auto_obj = Auto()
    auto_obj.load_json(db_data)
    return auto_obj.serialize()


def create_new(params):
    """
    Create a new car
    :param params:
    :return:
    """
    auto = Auto()
    auto.load_json(params)
    auto.generate_vin()

    id_ = database.insert_document(auto_collection, auto.serialize())
    auto._id = str(id_)
    return auto.serialize()


def update(params):
    """
    Update a car
    :param params:
    :return:
    """
    id_ = params['id']

    auto = get_one(id_)
    for item in params:
        auto[item] = params[item]

    del auto['_id']

    database.update_document(auto_collection, {'_id': ObjectId(id_)}, auto)

    return auto


def delete(id_):
    auto = get_one(id_)

    database.delete_document(auto_collection, {'_id': ObjectId(id_)})

    return True
