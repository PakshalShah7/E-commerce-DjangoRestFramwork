from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from ecommerce.pagination import CustomLimitOffsetPagination
from user.models import User, UserAddress
from user.serializers import UserSerializer, UserAddressSerializer, ChangePasswordSerializer


class SignupView(CreateAPIView):
    """
    This class will create new user instance.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(KnoxLoginView):
    """
    This class will authenticate and authorized the requested user if user input correct credentials.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
        This method will log in the user with Token.
        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserRetrieveUpdateDestroyView(UserPassesTestMixin, SingleObjectMixin, RetrieveUpdateDestroyAPIView):
    """
    This class will retrieve details, update or delete user if user is authenticated.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'email', 'contact_number', 'first_name', 'last_name',
                        'is_superuser', 'is_staff', 'date_joined']

    def test_func(self):
        """
        This method will check whether user has permission or not.
        """
        instance = self.get_object()
        if instance.id == self.request.user.id:
            return True


class UserListView(ListAPIView):
    """
    Returns a list of all users only if user is superuser.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomLimitOffsetPagination


class UserAddressView(ModelViewSet):
    """
    ModelViewSet for user address model provides the following actions.

    create: Create a new user address instance.
    retrieve: Return the given user address.
    update: Update the given user address instance.
    partial_update: Partially update the given user address instance.
    destroy: Deletes the given user address instance.
    list: Return a list of all existing user addresses.
    """
    serializer_class = UserAddressSerializer
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['id', 'user', 'address_type']

    def get_queryset(self):
        """
        Returns a list of all user address if user is superuser or staff otherwise return user's
        addresses itself.
        """
        if self.request.user.is_superuser or self.request.user.is_staff:
            queryset = UserAddress.objects.all()
        else:
            queryset = UserAddress.objects.filter(user=self.request.user)
        return queryset


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        """
        This method will retrieve required object.
        """
        return self.request.user
