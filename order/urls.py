from django.urls import path
from order.views import OrderListView, OrderStatusUpdateView, OrderInvoiceListView, OrderInvoiceDetailView, \
    OrderCreateView

app_name = 'order'

urlpatterns = [

    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('order-update/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-update'),
    path('invoice-list/', OrderInvoiceListView.as_view(), name='invoice-list'),
    path('invoice-detail/<int:pk>/', OrderInvoiceDetailView.as_view(), name='invoice-detail')

]
