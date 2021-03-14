from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):

    def test_profile_form(self):
        form = UserProfileForm({'user': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors.keys())
        self.assertEqual(form.errors['user'][0], 'This field is required')
