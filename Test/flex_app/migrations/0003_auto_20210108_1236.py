# Generated by Django 3.1.5 on 2021-01-08 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex_app', '0002_remove_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]
