#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models import storage


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_additional_parameter(self):
        """Tests and validates acceptance of additional parameters"""
        new_r = Review()
        storage.save()
        new_r.__dict__.update({'user_id': '00017'})
        storage._update(new_r)
        self.assertTrue('user_id' in new_r.__dict__.keys())
