# Generated by Django 3.2.19 on 2023-06-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
