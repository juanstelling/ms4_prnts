from django.test import TestCase
from .models import Subscribe


class TestNewsletterModel(TestCase):

    def test_email_label(self):
        # Get an profile object to test
        subscribe = Subscribe.objects.get(id=1)

        # get the metadata for the field and use it to query the field data
        field_label = subscribe._meta.get_field('email').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'email')

    def test_default_full_name_max_length(self):
        subscribe = Subscribe.objects.get(id=1)
        max_length = subscribe._meta.get_field('email').max_length
        self.assertEqual(max_length, 255)

    def test_timestamp_label(self):
        subscribe = Subscribe.objects.get(id=1)
        field_label = subscribe._meta.get_field('timestamp').verbose_name
        self.assertEqual(field_label, 'timestamp')

    def test_contact_str_method(self):
        subscribe = Subscribe.objects.create(name='test newsletter')
        self.assertEqual(str(subscribe), 'test newsletter')
