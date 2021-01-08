# Generated by Django 3.1.5 on 2021-01-07 12:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=20)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('password', models.CharField(help_text='Use \'[algo]$[salt]$[hexdigest]\' or use the <a href="password/">change password form</a>.', max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flex_app.role')),
            ],
        ),
    ]