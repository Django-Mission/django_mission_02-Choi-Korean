# Generated by Django 4.0.3 on 2022-04-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_remove_faq_modified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]