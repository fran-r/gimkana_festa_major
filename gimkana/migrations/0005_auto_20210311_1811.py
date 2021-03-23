# Generated by Django 3.1.6 on 2021-03-11 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gimkana', '0004_auto_20210220_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qrscan',
            options={'ordering': ['qr_id', 'scanned_by']},
        ),
        migrations.AlterField(
            model_name='qrscan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='qrscan',
            name='qr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qr_id', to='gimkana.qr'),
        ),
        migrations.AlterField(
            model_name='qrscan',
            name='scanned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanned_by', to='auth.user'),
        ),
        migrations.AlterUniqueTogether(
            name='qrscan',
            unique_together={('qr_id', 'scanned_by')},
        ),
        migrations.CreateModel(
            name='UserQr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('L', 'Locked'), ('U', 'Unlocked'), ('S', 'Scanned')], default='L', help_text='QR status', max_length=1)),
                ('scanned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
