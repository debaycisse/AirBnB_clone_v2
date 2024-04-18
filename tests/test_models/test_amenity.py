#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models import storage


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_additional_parameter(self):
        """Tests and validates acceptance of additional parameters"""
        new_am = Amenity()
        storage.save()
        new_am.__dict__.update({'place_id': '00011'})
        storage._update(new_am)
        self.assertTrue('place_id' in new_am.__dict__.keys())
