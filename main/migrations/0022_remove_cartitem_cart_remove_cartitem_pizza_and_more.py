# Generated by Django 4.2.13 on 2024-06-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_cartitem_pizza_name_cartitem_pizza_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='pizza',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
