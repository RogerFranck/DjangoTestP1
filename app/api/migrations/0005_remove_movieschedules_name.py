# Generated by Django 4.0.2 on 2022-02-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_ticketsold_alter_drink_price_alter_food_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieschedules',
            name='name',
        ),
    ]