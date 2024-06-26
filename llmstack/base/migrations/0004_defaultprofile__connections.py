# Generated by Django 4.2.1 on 2023-10-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_defaultprofile_anthropic_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultprofile',
            name='_connections',
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text='Encrypted connections config to use with processors',
                null=True),
        ),
    ]
