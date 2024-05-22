import json
import pickle

import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, house_size, bed, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except Exception:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = house_size
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    global __locations
    load_data()
    __locations = [location.title() for location in __locations]
    return __locations


def load_data():
    print("Loadding data...")
    global __data_columns
    global __locations

    with open("usa/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    global __model
    with open("usa/model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Data loaded...")

    return __data_columns, __locations, __model


if __name__ == "__main__":
    print(get_location_names())
    print(get_estimated_price("escondido", 1000, 2, 2))
    print(get_estimated_price("roseville", 1000, 3, 3))
