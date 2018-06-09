# Generated by Django 2.0 on 2018-06-08 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_booking', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of booking')),
                ('date_starting', models.DateField(verbose_name='Date of start of tenancy')),
                ('date_ending', models.DateField(null=True, verbose_name='Date of end of tenancy')),
                ('payment_status', models.BooleanField(default=False, verbose_name='Is payment made')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property', verbose_name='Property Details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Booking')),
            ],
            options={
                'ordering': ('time_booking', 'date_starting', 'property'),
            },
        ),
    ]