# Generated by Django 2.2.6 on 2019-11-03 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_markup_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='markup_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='container.MarkupKey'),
        ),
    ]