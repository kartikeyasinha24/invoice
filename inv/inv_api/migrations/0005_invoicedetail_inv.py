# Generated by Django 4.2.3 on 2023-08-11 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv_api', '0004_remove_invoicedetail_inv'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='inv',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, to='inv_api.invoice'),
            preserve_default=False,
        ),
    ]
