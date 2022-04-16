from django.db import models
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.contrib.auth import get_user_model  # 장고(인증시스템)에서 사용하고 있는 유저모델

# Create your models here.

User = get_user_model()

class Faq(models.Model):
    head = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True) # verbose_name : 관리자나 폼 등 일반 사용자쪽 페이지에 노출될 필드에 대한 이름 지정
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # auto_now_add=True : 게시글 작성시 자동 날짜 입력
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    pass