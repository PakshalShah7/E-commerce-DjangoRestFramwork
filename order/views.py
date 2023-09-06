from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from ecommerce.pagination import CustomLimitOffsetPagination
from order.models import Order, OrderInvoice
from order.serializers import OrderSerializer, OrderInvoiceSerializer


class OrderCreateView(CreateAPIView):
    """
    This view will create new order instance.
    """
    serializer_class = OrderSerializer


class OrderListView(ListAPIView):
    """
    Returns a list of all orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['order', 'user', 'status']


class OrderStatusUpdateView(UpdateAPIView):
    """
    This view will update an order status and order invoice.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """
        Returns an order that is specific to user.
        """
        return Order.objects.filter(status='Confirmed')

    def update(self, request, *args, **kwargs):
        """
        This method updates a model instance.
        """
        order = Order.objects.get(user=self.request.user, status='Confirmed')
        if order.status == 'Delivered':
            order_invoice = OrderInvoice.objects.get(user=self.request.user, order=order)
            order_invoice.status = 'Successful'
            order_invoice.save()
        elif order.status == 'Cancelled':
            order_invoice = OrderInvoice.objects.get(user=self.request.user, order=order)
            order_invoice.status = 'Cancelled'
            order_invoice.save()
        return super(OrderStatusUpdateView, self).update(request, *args, **kwargs)


class OrderInvoiceListView(ListAPIView):
    """
    Returns a list of all order invoices.
    """
    serializer_class = OrderInvoiceSerializer
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['user', 'order', 'status']

    def get_queryset(self):
        """
        Returns a list of all order invoices if user is superuser or staff otherwise return user's order
        invoices itself.
        """
        if self.request.user.is_superuser or self.request.user.is_staff:
            queryset = OrderInvoice.objects.all()
        else:
            queryset = OrderInvoice.objects.filter(user=self.request.user)
        return queryset


class OrderInvoiceDetailView(UserPassesTestMixin, SingleObjectMixin, RetrieveAPIView):
    """
    Returns detail of order invoice.
    """
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer

    def get_queryset(self):
        """
        Returns a list of all order invoices if user is superuser or staff otherwise return user's order
        invoices itself.
        """
        if self.request.user.is_superuser or self.request.user.is_staff:
            queryset = OrderInvoice.objects.all()
        else:
            queryset = OrderInvoice.objects.filter(user=self.request.user)
        return queryset

    def test_func(self):
        """
        This method will check whether user has permission or not.
        """
        instance = self.get_object()
        if instance.user.id == self.request.user.id:
            return True
