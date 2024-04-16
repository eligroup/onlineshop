from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


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
        self.assertEqual(self.User.objects.all()[0].username, self.user1.username)
        self.assertEqual(self.User.objects.all()[1].username, 'user2')
        self.assertEqual(self.User.objects.all()[0].email, self.user1.email)
        self.assertEqual(self.User.objects.all()[1].email, 'user2@user2.com')
        self.assertEqual(self.user1.username, 'user1')
        self.assertEqual(self.user2.username, 'user2')
        self.assertEqual(self.user1.email, 'user1@user1.com')
        self.assertEqual(self.user2.email, 'user2@user2.com')

    def test_signup_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)

    def test_signup_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)

    def test_signup_by_body(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'sign up')

    def test_signup_by_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_login_by_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code,200)

    def test_login_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_login_by_body(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'login')

    def test_login_by_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, "registration/login.html")


