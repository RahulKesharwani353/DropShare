# Generated by Django 4.1.3 on 2022-11-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_folders_access_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='access_by',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
