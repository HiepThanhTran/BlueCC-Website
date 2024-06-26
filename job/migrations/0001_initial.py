# Generated by Django 5.0.3 on 2024-04-02 17:57

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary_start', models.IntegerField()),
                ('salary_end', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('requirements', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('benefits', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('position', models.CharField(max_length=50)),
                ('experience_year', models.CharField(max_length=20)),
                ('number_of_recruits', models.IntegerField(null=True)),
                ('work_form', models.CharField(choices=[('PART_TIME', 'Bán thời gian'), ('FULL_TIME', 'Toàn thời gian'), ('BOTH', 'Cả hai')], max_length=20)),
                ('gender', models.CharField(choices=[('MALE', 'Nam'), ('FEMALE', 'Nữ'), ('BOTH', 'Cả hai'), ('UNKNOWN', 'Không yêu cầu')], max_length=20, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jds', to='company.company')),
                ('users', models.ManyToManyField(related_name='jobs', through='job.JobApplication', to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobdescription'),
        ),
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together={('user', 'job')},
        ),
    ]
