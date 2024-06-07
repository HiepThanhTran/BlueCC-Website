# Generated by Django 5.0.3 on 2024-04-02 17:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.BooleanField(blank=True, choices=[('M', 'Male'), ('F', 'FEMALE')], null=True)),
            ],
        ),
    ]
