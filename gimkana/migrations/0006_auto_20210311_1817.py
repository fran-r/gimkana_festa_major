# Generated by Django 3.1.6 on 2021-03-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimkana', '0005_auto_20210311_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrscan',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
