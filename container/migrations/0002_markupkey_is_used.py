# Generated by Django 2.2.6 on 2019-11-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='markupkey',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
