# Generated by Django 4.0.4 on 2022-05-14 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoniApp', '0003_alter_pedido_prestamo_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_prestamo',
            name='monto',
            field=models.IntegerField(max_length=50),
        ),
    ]
