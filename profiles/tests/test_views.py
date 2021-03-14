from django.test import TestCase


class TestProfilesViews(TestCase):

    def test_profile_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
