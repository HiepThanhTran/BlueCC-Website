# Generated by Django 5.0.3 on 2024-04-02 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=254, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='user.user')),
            ],
        ),
    ]
