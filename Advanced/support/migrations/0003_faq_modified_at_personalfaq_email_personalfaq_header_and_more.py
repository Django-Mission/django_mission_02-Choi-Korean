# Generated by Django 4.0.4 on 2022-04-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_rename_comment_faqcomment_personalfaq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='personalfaq',
            name='email',
            field=models.CharField(default=None, max_length=3, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='personalfaq',
            name='header',
            field=models.TextField(default='', verbose_name='제목'),
        ),
        migrations.AddField(
            model_name='personalfaq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
        migrations.AddField(
            model_name='personalfaq',
            name='phone_number',
            field=models.CharField(default=None, max_length=3, verbose_name='전화번호'),
        ),
    ]
