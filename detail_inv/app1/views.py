from django.shortcuts import render

# Create your views here.
# invoice_app/views.py
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
"""
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
"""

# invoice_app/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create the invoice
        self.perform_create(serializer)

        # Create associated invoice details
        invoice = serializer.instance
        detail_data = request.data.get('details', [])
        for detail_item in detail_data:
            detail_item['invoice_no'] = invoice.id
            detail_serializer = InvoiceDetailSerializer(data=detail_item)
            detail_serializer.is_valid(raise_exception=True)
            detail_serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
