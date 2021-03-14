from django.test import TestCase
from .models import Product


class TestModel(TestCase):

    """ Product Model testing  """



    def test_product_booleanfields_defaults(self):
        product = Product.objects.create(name='test product')
        self.assertTrue(product.in_stock)
 
    def test_product_str_method(self):
        product = Product.objects.create(name='test product')
        self.assertEqual(str(product), 'test product')

