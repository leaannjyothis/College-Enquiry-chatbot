# Generated by Django 4.1 on 2022-12-11 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Bot', '0008_registration_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='dept',
            new_name='meal_preference',
        ),
    ]
