# Generated by Django 3.2 on 2021-05-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='loc',
            field=models.CharField(default='.', max_length=200),
        ),
    ]