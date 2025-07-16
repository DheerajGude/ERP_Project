from django.test import TestCase
# pylint: disable=no-member

# Create your tests here.
from django.test import TestCase
from erp_analytics.models.customer import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(name="Test Customer", email="test@example.com")

    def test_customer_creation(self):
        customer = Customer.objects.get(name="Test Customer")
        self.assertEqual(customer.email, "test@example.com")
