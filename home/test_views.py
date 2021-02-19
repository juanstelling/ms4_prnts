from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'home/includes/about-info.html')
        self.assertTemplateUsed(response, 'home/includes/header-images.html')
        self.assertTemplateUsed(response, 'home/includes/new-products.html')
        self.assertTemplateUsed(response, 'home/includes/newsletter.html')
        self.assertTemplateUsed(response, 'home/includes/usp.html')
