# Generated by Django 3.0.5 on 2020-05-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20200503_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_image'),
        ),
    ]
