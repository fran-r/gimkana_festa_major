# Generated by Django 3.1.6 on 2021-03-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimkana', '0006_auto_20210311_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrscan',
            name='_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='qrscan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
