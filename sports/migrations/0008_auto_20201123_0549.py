# Generated by Django 3.1.2 on 2020-11-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0007_auto_20201120_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportlist',
            name='quoteOne',
        ),
        migrations.RemoveField(
            model_name='sportlist',
            name='quoteTwo',
        ),
        migrations.AddField(
            model_name='sportlist',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
