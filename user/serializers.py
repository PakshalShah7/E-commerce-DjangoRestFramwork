""" This file contains user and user address serializers which are used in project. """

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import User, UserAddress
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    """
    This is model serializer for user model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserAddressSerializer(serializers.ModelSerializer):
    """
    This is model serializer for user address model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = UserAddress
        fields = ['id', 'address', 'pincode', 'city', 'state', 'address_type']

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        new_address = UserAddress.objects.create(user=self.context['request'].user,
                                                 address=validated_data['address'],
                                                 pincode=validated_data['pincode'],
                                                 city=validated_data['city'],
                                                 state=validated_data['state'],
                                                 address_type=validated_data['address_type'])
        return new_address


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    This is model serializer for changing password.
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        """
        This method validates that password and password2 matches or not.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        """
        This method validates that old password is correct or not.
        """
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        """
        This method will update password.
        """
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    This function will send email for password reset.
    """
    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key)
    send_mail(
        "Password Reset for {title}".format(title="E-commerce Website"),
        email_plaintext_message,
        "pakshal.shah@trootech.com",
        [reset_password_token.user.email]
    )
