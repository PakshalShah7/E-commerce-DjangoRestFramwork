from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import ProductView

app_name = 'product'

router = SimpleRouter()
router.register(r'products', ProductView, basename='products')

urlpatterns = [

    path('', include(router.urls))

]
