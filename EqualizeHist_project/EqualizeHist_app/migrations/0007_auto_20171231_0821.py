# Generated by Django 2.0 on 2017-12-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EqualizeHist_app', '0006_auto_20171230_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histogram',
            name='imageHist',
            field=models.ImageField(upload_to=''),
        ),
    ]
