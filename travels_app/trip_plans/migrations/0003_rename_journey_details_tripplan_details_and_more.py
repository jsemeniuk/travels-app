# Generated by Django 4.1.4 on 2023-05-11 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip_plans', '0002_alter_tripplan_lists_alter_tripplan_places'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripplan',
            old_name='journey_details',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='tripplan',
            name='trip_details',
        ),
    ]
