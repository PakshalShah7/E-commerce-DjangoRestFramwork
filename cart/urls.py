from django.urls import path, include
from rest_framework.routers import SimpleRouter
from cart.views import CartItemView, CartListView

app_name = 'cart'

router = SimpleRouter()
router.register(r'cart-items', CartItemView, basename='cart-items')

urlpatterns = [

    path('', include(router.urls)),
    path('cart/', CartListView.as_view(), name='cart')

]
