from django.test import TestCase


class TestContactViews(TestCase):

    """ All contact view testing  """

    def test_contact_view(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
