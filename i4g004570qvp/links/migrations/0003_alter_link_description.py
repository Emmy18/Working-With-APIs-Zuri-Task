# Generated by Django 4.0.5 on 2022-06-29 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(default='Link Description', max_length=200),
        ),
    ]
