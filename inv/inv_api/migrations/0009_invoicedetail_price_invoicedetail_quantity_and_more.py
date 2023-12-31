# Generated by Django 4.2.3 on 2023-08-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv_api', '0008_alter_invoicedetail_inv'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='price',
            field=models.DecimalField(decimal_places=1, default=10, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='unitprice',
            field=models.DecimalField(decimal_places=1, default=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='description',
            field=models.TextField(),
        ),
    ]
