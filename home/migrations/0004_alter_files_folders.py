# Generated by Django 4.1.3 on 2022-11-20 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_folders_access_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='folders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='home.folders'),
        ),
    ]
