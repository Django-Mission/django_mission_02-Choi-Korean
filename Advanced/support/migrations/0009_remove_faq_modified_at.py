# Generated by Django 4.0.3 on 2022-04-17 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0008_faq_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='modified_at',
        ),
    ]
