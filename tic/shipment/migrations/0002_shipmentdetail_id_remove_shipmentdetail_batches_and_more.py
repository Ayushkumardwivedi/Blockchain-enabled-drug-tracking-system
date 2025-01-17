# Generated by Django 4.2.16 on 2024-11-15 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='shipmentdetail',
            name='batches',
        ),
        migrations.AlterField(
            model_name='shipmentdetail',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_batches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shipmentdetail',
            name='shipment',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='shipmentdetail',
            name='batches',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
