# Generated by Django 4.0.4 on 2022-04-16 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='FaqComment',
        ),
        migrations.CreateModel(
            name='PersonalFaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiries', models.CharField(choices=[('일반', 'normal'), ('계정', 'id'), ('기타', 'ect')], default='일반', max_length=3)),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.personalfaq')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
