# Generated by Django 4.2.2 on 2023-07-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]