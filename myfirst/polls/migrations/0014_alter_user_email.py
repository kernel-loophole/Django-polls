# Generated by Django 3.2.6 on 2021-09-01 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
