from django.test import TestCase
from .models import Flower
from django.contrib.auth import get_user_model

# Create your tests here.
class FlowersTests(TestCase):


  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
    testuser1.save()

    test_flower = Flower.objects.create(name= "rake",owner=testuser1, description="Testing to see!!")
    test_flower.save()


  def test_flowers_model(self):
    flower = Flower.objects.get(id=1)
    actual_owner = str(flower.owner)
    actual_name = str(flower.name)
    actual_description = str(flower.description)
    self.assertEqual(actual_owner, "testuser1")
    self.assertEqual(actual_name, "rake")
    self.assertEqual(actual_description, "Testing testing!")