from django.urls import path, include
from rest_framework.routers import SimpleRouter
from category.views import CategoryView

app_name = 'category'

router = SimpleRouter()
router.register(r'categories', CategoryView, basename='categories')

urlpatterns = [

    path('', include(router.urls))

]
