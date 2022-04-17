from django.db import models
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.contrib.auth import get_user_model
from django.forms import RegexField  # 장고(인증시스템)에서 사용하고 있는 유저모델

# Create your models here.

User = get_user_model()

class Faq(models.Model):
    INQUIRIES_CHOICES = [
        ('일반', 'normal'),
        ('계정', 'id'),
        ('기타', 'ect'),
    ]
    inquiries = models.CharField(max_length=3, choices=INQUIRIES_CHOICES, default='일반')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # auto_now_add=True : 게시글 작성시 자동 날짜 입력
    modified_on = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    # modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

class FaqComment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Faq', on_delete=models.CASCADE)   # 게시글 foreignKey 연결. 게시글이 삭제되면 댓글도 삭제되게 on_delete에 CASCADE 설정
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE) # 사용자 연결. 장고에서 만든 사용자 모델 연결

class PersonalFaq(models.Model):
    INQUIRIES_CHOICES = [
        ('일반', 'normal'),
        ('계정', 'id'),
        ('기타', 'ect'),
    ]
    inquiries = models.CharField(max_length=3, choices=INQUIRIES_CHOICES, default='일반')
    head = models.TextField(verbose_name='제목', default='')
    content = models.TextField(verbose_name='내용')
    email = models.CharField(max_length=3, verbose_name='이메일', default=None)
    phone_number = models.CharField(max_length=3, verbose_name='전화번호', default=None)
    image = models.ImageField(verbose_name='이미지', null=True, blank=True) # verbose_name : 관리자나 폼 등 일반 사용자쪽 페이지에 노출될 필드에 대한 이름 지정
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # auto_now_add=True : 게시글 작성시 자동 날짜 입력
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

class PersonalComment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='PersonalFaq', on_delete=models.CASCADE)   # 게시글 foreignKey 연결. 게시글이 삭제되면 댓글도 삭제되게 on_delete에 CASCADE 설정
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE) # 사용자 연결. 장고에서 만든 사용자 모델 연결