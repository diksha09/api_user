# Generated by Django 2.1 on 2019-06-26 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUserDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('socialId', models.CharField(default='', max_length=255)),
                ('role', models.IntegerField()),
                ('profile_pic', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(default='m', max_length=1)),
                ('address', models.CharField(default='', max_length=255)),
                ('idType', models.CharField(default='', max_length=255)),
                ('idNumber', models.CharField(default='', max_length=255)),
                ('status', models.IntegerField(default=1)),
                ('designationName', models.CharField(default='', max_length=255)),
                ('onOffNotification', models.IntegerField(default=1)),
                ('user_auth', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'otheruserdetails',
            },
        ),
    ]