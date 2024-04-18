#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models import storage


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_additional_parameter(self):
        """Tests and validates acceptance of additional parameters"""
        new_city = City()
        storage.save()
        new_city.__dict__.update({'state_id': '005538'})
        storage._update(new_city)
        self.assertTrue('state_id' in new_city.__dict__.keys())
