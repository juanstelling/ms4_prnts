from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_form(self):
        form = ContactForm({
            'full_name': '',
            'email': '',
            'messages': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('messages', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required')
        self.assertEqual(form.errors['email'][0], 'This field is required')
        self.assertEqual(form.errors['messages'][0], 'This field is required')
