# Generated by Django 4.1.7 on 2023-03-16 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_user_options_user_birth_date_and_more'),
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.CharField(editable=False, max_length=10, null=True)),
                ('total_amount', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='cart.cart')),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='myaddress', to='user.useraddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failure', 'Failure')], default='Pending', max_length=7)),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_address', to='user.useraddress')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
