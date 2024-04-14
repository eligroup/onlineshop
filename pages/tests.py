from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_homepage_by_name(self):
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_homepage_by_url(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_by_template(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,'home.html')

    def test_homepage_by_body(self):
        response=self.client.get('/')
        self.assertContains(response,"home page!!!")

    def test_aboutus_by_name(self):
        response=self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code,200)

    def test_aboutus_by_template(self):
        response=self.client.get('/about_us/')
        self.assertTemplateUsed(response,'pages/about_us.html')

    def test_aboutus_by_url(self):
        response=self.client.get("/about_us/")
        self.assertEqual(response.status_code,200)

    def test_aboutus_by_body(self):
        response=self.client.get(reverse('about_us'))
        self.assertContains(response,"about us!!!")





