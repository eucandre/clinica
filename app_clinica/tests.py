from django.test import TestCase
from app_clinica.models import *
import unittest

class DesntistaTestCase(unittest.TestCase):
    def setUp(self):
        self.andre = Dentista.objects.create(name = "andre", date_register="2016-11-12")



