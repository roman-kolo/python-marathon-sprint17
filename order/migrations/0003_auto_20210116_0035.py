# Generated by Django 3.1.5 on 2021-01-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210116_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
