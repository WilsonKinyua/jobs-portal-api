# Generated by Django 3.2.7 on 2022-04-23 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(default='fa fa-briefcase', max_length=200)),
                ('description', models.TextField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('company_email', models.EmailField(max_length=100)),
                ('company_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('company_website', models.URLField(default='', max_length=1000)),
                ('company_linkedin', models.URLField(default='', max_length=1000)),
                ('company_logo', models.TextField(blank=True, null=True)),
                ('company_location', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('salary_range', models.CharField(default='', max_length=1000)),
                ('job_type', models.CharField(default='Full Time', max_length=1000)),
                ('job_description', models.TextField(default='', max_length=5000)),
                ('location', models.CharField(default='', max_length=1000)),
                ('application_deadline', models.DateField()),
                ('experience', models.IntegerField(default=0)),
                ('qualification', models.CharField(default='', max_length=1000)),
                ('link_to_job', models.URLField(default='', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
