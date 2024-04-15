from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user1 = cls.User.objects.create_user(username="user1", email="user1@user1.com")
        cls.user2 = cls.User.objects.create_user(username="user2", email="user2@user2.com")
    # second way
    # def setUp(self):
    #     self.User=get_user_model()
    #     self.user1=self.User.objects.create_user(username="user1", email="user1@user1.com")
    #     self.user2 = self.User.objects.create_user(username="user2", email="user2@user2.com")
    # in class method objects will be saved one time before running all tests
    # in setUp(self) objects will be saved before running each test for 5 test ,5 times will be saved
    def test_custom_user(self):
        self.assertEqual(self.User.objects.all().count(),2)
        self.assertEqual(self.User.objects.all()[0].username, 'user1')
        self.assertEqual(self.User.objects.all()[1].username, 'user2')
        self.assertEqual(self.User.objects.all()[0].email, 'user1@user1.com')
        self.assertEqual(self.User.objects.all()[1].email, 'user2@user2.com')
        self.assertEqual(self.user1.username, 'user1')
        self.assertEqual(self.user2.username, 'user2')
        self.assertEqual(self.user1.email, 'user1@user1.com')
        self.assertEqual(self.user2.email, 'user2@user2.com')


