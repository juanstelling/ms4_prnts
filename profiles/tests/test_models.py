from django.test import TestCase
from .models import UserProfile


class Test_Profiles_Model(TestCase):

    """ full name testing  """

    def test_default_full_name_label(self):
        # Get an profile object to test
        profile = UserProfile.objects.get(id=1)

        # get the metadata for the field and use it to query the field data
        field_label = profile._meta.get_field('default_full_name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'default_full_name')

    def test_default_full_name_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_full_name').max_length
        self.assertEqual(max_length, 50)

    """ phone number testing  """

    def test_default_phone_number_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_phone_number').verbose_name
        self.assertEqual(field_label, 'default_phone_number')

    def test_default_phone_number_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    """ country testing  """

    def test_default_country_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_country').verbose_name
        self.assertEqual(field_label, 'default_country')

    """ postcode testing  """

    def test_default_postcode_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_postcode').verbose_name
        self.assertEqual(field_label, 'default_postcode')

    def test_default_postcode_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_postcode').max_length
        self.assertEqual(max_length, 20)

    """ town or city testing  """

    def test_default_town_or_city_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_town_or_city').verbose_name
        self.assertEqual(field_label, 'default_town_or_city')

    def test_default_town_or_city_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_town_or_city').max_length
        self.assertEqual(max_length, 40)

    """ street addresses 1 and 2 testing  """

    def test_default_street_address1_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_street_address1').verbose_name
        self.assertEqual(field_label, 'default_street_address1')

    def test_default_street_address1_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field(
            'default_street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_default_street_address2_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field(
            'default_street_address2').verbose_name
        self.assertEqual(field_label, 'default_street_address2')

    def test_default_street_address2_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field(
            'default_street_address2').max_length
        self.assertEqual(max_length, 80)

    def test_profile_str_method(self):
        profile = UserProfile.objects.create(name='test profile')
        self.assertEqual(str(profile), 'test profile')
