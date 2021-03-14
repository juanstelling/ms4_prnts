from django.test import TestCase
from .models import Product


class TestProductViews(TestCase):

    """ All products view testing  """

    def test_get_all_products_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    """ sorting price and name testing  """

    def test_all_product_sort_price_asc(self):
        response = self.client.get(
            '/products/?page=1&sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_product_sort_price_desc(self):
        response = self.client.get(
            '/products/?page=1&sort=price&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_product_sort_name_asc(self):
        response = self.client.get(
            '/products/?page=1&sort=name&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_product_sort_name_desc(self):
        response = self.client.get(
            '/products/?page=1&sort=name&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    """ Categories testing   """
 
    def test_category_black_and_white_view(self):
        response = self.client.get(
            '/products/?category=black_and_white')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_landscape_view(self):
        response = self.client.get(
            '/products/?category=landscape')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_paint_view(self):
        response = self.client.get(
            '/products/?category=paint')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_streetart_view(self):
        response = self.client.get(
            '/products/?category=streetart')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    """ Product detail testing  """

    def test_product_detail_view(self):
        product = Product.objects.create(name='Test product id')
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')




