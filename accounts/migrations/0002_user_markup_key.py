# Generated by Django 2.2.6 on 2019-11-03 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0002_markupkey_is_used'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='markup_key',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='container.MarkupKey'),
            preserve_default=False,
        ),
    ]