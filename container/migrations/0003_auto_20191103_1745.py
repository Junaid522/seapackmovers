# Generated by Django 2.2.6 on 2019-11-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0002_markupkey_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markupkey',
            name='markup_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
