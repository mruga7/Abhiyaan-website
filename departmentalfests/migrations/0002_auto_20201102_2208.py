# Generated by Django 3.1.2 on 2020-11-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentalfests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='procedure',
            field=models.TextField(blank=True),
        ),
    ]