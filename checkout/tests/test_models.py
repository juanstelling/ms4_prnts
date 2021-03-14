from django.test import TestCase
from .models import Order, OrderLineItem


class TestOrderModel(TestCase):

    """ Order number testing  """

    def test_order_number_label(self):
        # Get an profile object to test
        order = Order.objects.get(id=1)

        # get the metadata for the field and use it to query the field data
        field_label = order._meta.get_field('order_number').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'order_number')

    def test_default_order_number_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_number').max_length
        self.assertEqual(max_length, 55)

    """ User Profile testing  """

    def test_user_profile_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user_profile').verbose_name
        self.assertEqual(field_label, 'user_profile')

    """ full name testing  """

    def test_full_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full_name')

    def test_full_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 55)

    """ email testing  """

    def test_email_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_email_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('email').max_length
        self.assertEqual(max_length, 255)

    """ phone number testing  """

    def test_phone_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone_number')

    def test_phone_number_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 18)

    """ country testing  """

    def test_country_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    """ postcode testing  """

    def test_postcode_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('postcode').verbose_name
        self.assertEqual(field_label, 'postcode')

    def test_postcode_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('postcode').max_length
        self.assertEqual(max_length, 15)

    """ Town or city testing  """

    def test_town_or_city_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('town_or_city').verbose_name
        self.assertEqual(field_label, 'town_or_city')

    def test_town_or_city_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('town_or_city').max_length
        self.assertEqual(max_length, 30)

    """ street address 2 testing  """

    def test_street_address1_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address1').verbose_name
        self.assertEqual(field_label, 'street_address1')

    def test_street_address1_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address1').max_length
        self.assertEqual(max_length, 80)

    """ street address 2 testing  """

    def test_street_address2_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address2').verbose_name
        self.assertEqual(field_label, 'street_address2')

    def test_street_address2_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address2').max_length
        self.assertEqual(max_length, 80)

    """ date testing  """

    def test_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    """ delivery cost testing  """

    def test_delivery_cost_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('delivery_cost').verbose_name
        self.assertEqual(field_label, 'delivery_cost')

    def test_delivery_cost_max_length(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('delivery_cost').max_length
        self.assertEqual(max_digits, 6)

    """ order total testing  """

    def test_order_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_total').verbose_name
        self.assertEqual(field_label, 'order_total')

    def test_order_total_max_length(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('order_total').max_length
        self.assertEqual(max_digits, 10)

    """ grand total testing  """

    def test_grand_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('grand_total').verbose_name
        self.assertEqual(field_label, 'grand_total')

    def test_grand_total_max_length(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('grand_total').max_length
        self.assertEqual(max_digits, 10)

    """ original bag testing  """

    def test_original_bag_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('original_bag').verbose_name
        self.assertEqual(field_label, 'original_bag')

    """ stripe pid testing  """

    def test_stripe_pid_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('stripe_pid').verbose_name
        self.assertEqual(field_label, 'stripe_pid')

    def test_stripe_pid_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('stripe_pid').max_length
        self.assertEqual(max_length, 254)

    def test_order_str_method(self):
        order = Order.objects.create(name='test order')
        self.assertEqual(str(order), 'test order')


class TestOrderLineItemModel(TestCase):

    def test_order_label(self):
        order = OrderLineItem.objects.get(id=1)
        field_label = order._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order')

    def test_product_label(self):
        order = OrderLineItem.objects.get(id=1)
        field_label = order._meta.get_field('product').verbose_name
        self.assertEqual(field_label, 'product')

    def test_quantity_label(self):
        order = OrderLineItem.objects.get(id=1)
        field_label = order._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_lineitem_total_label(self):
        order = OrderLineItem.objects.get(id=1)
        field_label = order._meta.get_field('lineitem_total').verbose_name
        self.assertEqual(field_label, 'lineitem_total')

    def test_lineitem_total_max_length(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('lineitem_total').max_length
        self.assertEqual(max_digits, 6)

    def test_orderlineitem_str_method(self):
        order = OrderLineItem.objects.create(name='test orderlineitem')
        self.assertEqual(str(order), 'test orderlineitem')
