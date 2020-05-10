# Generated by Django 3.0.4 on 2020-03-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200322_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='event',
            name='organizer_decription',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
