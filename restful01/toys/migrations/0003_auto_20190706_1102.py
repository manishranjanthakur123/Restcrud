# Generated by Django 2.2.3 on 2019-07-06 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_auto_20190706_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toy',
            old_name='was_included_inhome',
            new_name='was_included_in_home',
        ),
    ]