# Generated by Django 4.0.5 on 2022-06-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(default='str', max_length=200),
        ),
    ]
