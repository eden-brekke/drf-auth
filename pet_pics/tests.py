from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PetPic

# Create your tests here.

class PetPicTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_pet_pic = PetPic.objects.create(
            name="Pumpkin",
            added_by=testuser1,
            description="Best baby kitty gorl",
            type_of_pet = 'cat',
            img = 'https://files.slack.com/files-pri/T039KG69K-F03HR69583U/punkers_n.jpg'
        )
        test_pet_pic.save()
    
    def setUp(self):
        self.client.login(username="testuser1", password="pass")
    
    def test_pet_pics_model(self):
        pet_pic = PetPic.objects.get(id=1)
        actual_added_by = str(pet_pic.added_by)
        actual_name = str(pet_pic.name)
        actual_description = str(pet_pic.description)
        actual_type_of_pet = str(pet_pic.type_of_pet)
        actual_img = str(pet_pic.img)
        self.assertEqual(actual_added_by, "testuser1")
        self.assertEqual(actual_name, "Pumpkin")
        self.assertEqual(
            actual_description, "Best baby kitty gorl"
        )
        self.assertEqual(actual_type_of_pet, 'cat')
        self.assertEqual(actual_img, 'https://files.slack.com/files-pri/T039KG69K-F03HR69583U/punkers_n.jpg')

    def test_get_pet_pic_list(self):
        url = reverse("pet_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pet_pic = response.data
        self.assertEqual(len(pet_pic), 1)
        self.assertEqual(pet_pic[0]["name"], "Pumpkin")

    def test_get_pet_pic_by_id(self):
        url = reverse("pet_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pet_pic = response.data
        self.assertEqual(pet_pic["name"], "Pumpkin")

    
    def test_create_pet(self):
        url = reverse("pet_list")
        data = {"added_by": 1, "name": "Jack", "description": "bestest boi", "type_of_pet": "cat", "img": "https://files.slack.com/files-pri/T039KG69K-F03J2RV1265/20220531_113022.jpg"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        pets = PetPic.objects.all()
        self.assertEqual(len(pets), 2)
        self.assertEqual(PetPic.objects.get(id=2).name, "Jack")

    def test_update_pet(self):
        url = reverse("pet_detail", args=(1,))
        data = {
            "added_by": 1,
            "name": "Jack",
            "description": "goodest boi",
            "type_of_pet": "cat",
            "img": "https://files.slack.com/files-pri/T039KG69K-F03J2RV1265/20220531_113022.jpg",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pet = PetPic.objects.get(id=1)
        self.assertEqual(pet.name, data["name"])
        self.assertEqual(pet.added_by.id, data["added_by"])
        self.assertEqual(pet.description, data["description"])
        self.assertEqual(pet.type_of_pet, data['type_of_pet'])
        self.assertEqual(pet.img, data["img"])

    def test_delete_pet(self):
        url = reverse("pet_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        pet_pics = PetPic.objects.all()
        self.assertEqual(len(pet_pics), 0)
        
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("pet_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
