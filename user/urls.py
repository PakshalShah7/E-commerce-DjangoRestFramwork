from django.urls import path, include
from knox.views import LogoutView, LogoutAllView
from rest_framework.routers import SimpleRouter
from user.views import UserAddressView, ChangePasswordView, LoginView, SignupView, UserListView, \
    UserRetrieveUpdateDestroyView


app_name = 'user'

router = SimpleRouter()
router.register(r'addresses', UserAddressView, basename='addresses')

urlpatterns = [

    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logout-all/', LogoutAllView.as_view(), name='knox_logoutall'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('user-list/', UserListView.as_view(), name='user_list')

]
