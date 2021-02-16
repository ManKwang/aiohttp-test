import json
import uuid
from typing import Dict


class Auto:
    _id: str
    vendor: str
    model_name: str
    year_issue: str
    color: str
    vin_code: str

    def load_data(self, vendor: str, model_name: str, year_issue: str, color: str,
                  is_new: bool = False):
        self.color = color
        self.year_issue = year_issue
        self.model_name = model_name
        self.vendor = vendor

        if is_new:
            self.generate_vin()

    def generate_vin(self):
        """
        Generates the vin code
        :return:
        """
        self.vin_code = uuid.uuid4().hex[:12].upper()

    def serialize(self) -> Dict:
        """
        Serializes the object
        :return: Dict
        """
        return self.__dict__

    def load_json(self, json_data):
        """
        Loads json
        :param json_data:
        :return:
        """

        for key in json_data:
            if key not in self.__annotations__.keys():
                continue

            self.__setattr__(key, self.__annotations__[key](json_data[key]))

    def load_json_string(self, json_string: str):
        """
        Loads json string
        :param json_string:
        :return:
        """
        self.load_json(json.loads(json_string))
