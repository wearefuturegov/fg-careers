# Generated by Django 2.2.4 on 2019-11-20 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0017_auto_20191106_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancypage',
            old_name='team',
            new_name='location',
        ),
    ]