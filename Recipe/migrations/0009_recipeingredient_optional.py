# Generated by Django 2.2.1 on 2019-05-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0008_auto_20190527_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='optional',
            field=models.BooleanField(default=False),
        ),
    ]
