# Generated by Django 2.2.17 on 2021-01-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netauto', '0007_automation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='status',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
