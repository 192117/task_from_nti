# Generated by Django 4.0.6 on 2022-07-17 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='surname')),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_workers', models.TextField(blank=True, verbose_name='id_workers')),
                ('title', models.CharField(blank=True, max_length=30, verbose_name='title')),
                ('description', models.TextField(default=True, verbose_name='description')),
                ('completion_date', models.DateTimeField(verbose_name='completion date')),
                ('owner', models.TextField(verbose_name='email_owner')),
            ],
        ),
    ]