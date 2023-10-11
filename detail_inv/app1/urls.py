from django.urls import path, include
from djongo import admin
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-details', InvoiceDetailViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
]