from django.test import TestCase

# Create your tests here.
tatus_code,from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data1 = {
            'date': '2023-10-10',
            'invoice_no': 'INV123',
            'customer_name': 'John Doe',
            'details': [{
                    'description': 'Product 1',
                    'quantity': 5,
                    'unit_price': 10.0,
                    'price': 50.0
                },
                {
                    'description': 'Product 2',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                }
            ]
        }
        """
        #self.invoice = Invoice.objects.create(**self.invoice_data)
        self.detail_data = {
            'invoice_no': self.invoice,
            'description': 'Product 1',
            'quantity': 5,
            'unit_price': 10.0,
            'price': 50.0,
        }
        #self.client.post('http://localhost:8000/api/invoices/', data=self.invoice_data, format='json')
        #self.client.post('http://localhost:8000/api/invoice-details/', data=self.detail_data, format='json')
        """
    def test_get_invoices(self):
        response = self.client.get('http://localhost:8000/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_invoice_with_details(self):

        response = self.client.post('http://localhost:8000/api/invoices/', data=self.invoice_data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the invoice and associated details are created
        self.assertEqual(Invoice.objects.count(), 1)
        invoice = Invoice.objects.first()
        print(invoice)
        self.assertEqual(invoice.customer_name, 'John Doe')
        self.assertEqual(invoice.details.count(), 2)

        # Verify the details of the first detail item
        detail1 = invoice.details.first()
        print(detail1)
        self.assertEqual(detail1.description, 'Product 1')
        self.assertEqual(detail1.quantity, 5)
        self.assertEqual(detail1.unit_price, 10.0)
        self.assertEqual(detail1.price, 50.0)

        # Verify the details of the second detail item
        detail2 = invoice.details.last()
        self.assertEqual(detail2.description, 'Product 2')
        self.assertEqual(detail2.quantity, 3)
        self.assertEqual(detail2.unit_price, 15.0)
        self.assertEqual(detail2.price, 45.0)

    def test_get_invoice_details(self):
        response = self.client.get('http://localhost:8000/api/invoice-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice_detail(self):
        response = self.client.get('http://localhost:8000/api/invoices/')
        print(response.data)
        data = {
            'description': 'Product 3',
            'quantity': 3,
            'unit_price': 15.0,
            'price': 45.0,
            'invoice_no': 'inv222',
        }
        response = self.client.post('http://localhost:8000/api/invoice-details/', data=data, format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    """
    def test_create_invoice(self):
        data = {
            'date': '2023-10-11',
            'invoice_no': 'INV124',
            'customer_name': 'Jane Smith',
        }
        response = self.client.post('http://localhost:8000/api/invoices/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_invoice_details(self):
        response = self.client.get('http://localhost:8000/api/invoice-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice_detail(self):
        response = self.client.get('http://localhost:8000/api/invoices/')
        print(response.data)
        data = {
            'description': 'Product 2',
            'quantity': 3,
            'unit_price': 15.0,
            'price': 45.0,
            'invoice_no': 'self.invoice_data1.id',
        }
        response = self.client.post('http://localhost:8000/api/invoice-details/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data1 = {
            'date': '2023-10-10',
            'invoice_no': 'INV123',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Product 1',
                    'quantity': 5,
                    'unit_price': 10.0,
                    'price': 50.0
                },
                {
                    'description': 'Product 2',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                }
            ]
        }

    def test_create_invoice_with_details(self):
        response = self.client.post('http://localhost:8000/api/invoices/', data=self.invoice_data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the invoice and associated details are created
        self.assertEqual(Invoice.objects.count(), 1)
        invoice = Invoice.objects.first()
        self.assertEqual(invoice.customer_name, 'John Doe')
        self.assertEqual(invoice.details.count(), 2)

        # Verify the details of the first detail item
        detail1 = invoice.details.first()
        self.assertEqual(detail1.description, 'Product 1')
        self.assertEqual(detail1.quantity, 5)
        self.assertEqual(detail1.unit_price, 10.0)
        self.assertEqual(detail1.price, 50.0)

        # Verify the details of the second detail item
        detail2 = invoice.details.last()
        self.assertEqual(detail2.description, 'Product 2')
        self.assertEqual(detail2.quantity, 3)
        self.assertEqual(detail2.unit_price, 15.0)
        self.assertEqual(detail2.price, 45.0)
        """