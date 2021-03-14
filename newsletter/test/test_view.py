from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import subscribe, email_list_signup


class TestBagViews(SimpleTestCase):

    def test_subscribe_resolves(self):
        url = reverse('subscribe')
        self.assertEqual(resolve(url).func, subscribe)

    def test_email_list_signup_resolves(self):
        url = reverse('email_list_signup')
        self.assertEqual(resolve(url).func, email_list_signup)
