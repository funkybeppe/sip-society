# Generated by Django 3.2.18 on 2023-05-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default='2023-05-24 08:28:55'),
        ),
    ]
