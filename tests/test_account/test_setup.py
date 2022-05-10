from django.urls import reverse

from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        return super(TestSetUp, self).setUp()

    def tearDown(self):
        return super(TestSetUp, self).tearDown()
