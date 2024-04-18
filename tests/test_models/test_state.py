#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import storage


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_additional_parameter(self):
        """Tests and validates acceptance of additional parameters"""
        new_state = State()
        storage.save()
        new_state.__dict__.update({'owner_id': '006544'})
        storage._update(new_state)
        self.assertTrue('owner_id' in new_state.__dict__.keys())
