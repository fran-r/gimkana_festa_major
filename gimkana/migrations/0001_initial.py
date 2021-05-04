# Generated by Django 3.1.6 on 2021-05-04 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Qr',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('hint1', models.TextField(blank=True, null=True)),
                ('hint2', models.TextField(blank=True, null=True)),
                ('map_url', models.URLField(blank=True, null=True)),
                ('num_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['num_order'],
            },
        ),
        migrations.CreateModel(
            name='UserQr',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hints', models.IntegerField(blank=True, default=0)),
                ('scan_date', models.DateTimeField(blank=True, null=True)),
                ('value', models.IntegerField(blank=True, default=5)),
                ('qr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimkana.qr')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['qr__num_order'],
                'unique_together': {('qr_id', 'user_id')},
            },
        ),
    ]
