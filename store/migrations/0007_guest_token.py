# Generated by Django 3.2.19 on 2023-06-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
