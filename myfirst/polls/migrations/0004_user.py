# Generated by Django 3.2.5 on 2021-08-14 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('passwd', models.CharField(max_length=200)),
            ],
        ),
    ]
