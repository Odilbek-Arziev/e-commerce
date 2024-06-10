# Generated by Django 4.2.2 on 2023-07-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_order_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Создан', 'Создан'), ('Принят в работу', 'Принят в работу'), ('В пути', 'В пути'), ('Доставлен', 'Доставлен')], default='Создан', max_length=255),
        ),
    ]
