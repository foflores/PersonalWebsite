# Generated by Django 3.2.8 on 2021-10-19 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('aboutMe', models.TextField()),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('show', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'dateCreated',
            },
        ),
    ]