# Generated by Django 3.2 on 2021-04-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_gridlayout'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridlayout',
            name='is_displyed',
            field=models.BooleanField(default=True),
        ),
    ]
