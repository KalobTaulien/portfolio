# Generated by Django 3.0.8 on 2020-07-06 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20200602_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediasettings',
            old_name='snapchat',
            new_name='twitter',
        ),
    ]
