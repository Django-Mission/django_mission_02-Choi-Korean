# Generated by Django 4.0.4 on 2022-04-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_rename_header_personalfaq_head_alter_faq_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='modified_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='수정일'),
        ),
    ]