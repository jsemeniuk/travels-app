# Generated by Django 4.1.4 on 2023-01-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_travels', '0004_alter_placesvisited_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesvisited',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='placesvisited',
            name='visit_date',
            field=models.DateField(blank=True),
        ),
    ]
