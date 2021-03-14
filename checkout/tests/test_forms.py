from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_contact_form(self):
        form = OrderForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'town_or_city': '',
            'country': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required')
        self.assertEqual(form.errors['email'][0], 'This field is required')
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required')
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required')
        self.assertEqual(form.errors['country'][0], 'This field is required')
