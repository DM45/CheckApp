# Generated by Django 2.0.4 on 2018-04-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_auto_20180422_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='role',
            field=models.TextField(blank=True, choices=[('ЦО', 'ЦО'), ('ЦЭС', 'ЦЭС')]),
        ),
    ]