from django.test import TestCase
from .models import ContactMessage


class Test_Contact_Model(TestCase):

    def test_full_name_label(self):
        # Get the contact object to test 
        contact = ContactMessage.objects.get(id=1)

        # Get the metadata for the required field and use it to query the required field data
        field_label = contact._meta.get_field('full_name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'full_name')

    def test_full_name_max_length(self):
        contact = ContactMessage.objects.get(id=1)
        max_length = contact._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_label(self):
        contact = ContactMessage.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_message_label(self):
        contact = ContactMessage.objects.get(id=1)
        field_label = contact._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')

    def test_contact_str_method(self):
        contact = ContactMessage.objects.create(name='test contact')
        self.assertEqual(str(contact), 'test contact')
