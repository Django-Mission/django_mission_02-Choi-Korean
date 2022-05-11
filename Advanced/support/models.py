from operator import mod
from django.db import models
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.contrib.auth import get_user_model
from django.forms import RegexField  # 장고(인증시스템)에서 사용하고 있는 유저모델

# Create your models here.
User = get_user_model()


# 내 실습 코드


# class Category(models.Model):
#     name = models.CharField(max_length=50, help_text="글 분류")
    
#     def __str__(self):
#         return self.name

# class Faq(models.Model):
#     INQUIRIES_CHOICES = [
#         ('일반', 'normal'),
#         ('계정', 'id'),
#         ('기타', 'ect'),
#     ]
#     inquiries = models.CharField(max_length=3, choices=INQUIRIES_CHOICES, default='일반')
#     content = models.TextField(verbose_name='내용')
#     created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # auto_now_add=True : 게시글 작성시 자동 날짜 입력
#     modified_on = models.DateTimeField(auto_now=True)
#     writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
#     modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Faq.writer+")
#     comment = models.TextField(verbose_name='답변', default='')

# class PersonalFaq(models.Model):
#     category = models.ManyToManyField(Category, help_text='선택해주세요.')
#     head = models.TextField(verbose_name='제목', default='')
#     content = models.TextField(verbose_name='내용')
#     email = models.CharField(max_length=3, verbose_name='이메일', default=None)
#     phone_number = models.CharField(max_length=3, verbose_name='전화번호', default=None)
#     image = models.ImageField(verbose_name='이미지', null=True, blank=True) # verbose_name : 관리자나 폼 등 일반 사용자쪽 페이지에 노출될 필드에 대한 이름 지정
#     created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # auto_now_add=True : 게시글 작성시 자동 날짜 입력
#     writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

# class PersonalComment(models.Model):
#     content = models.TextField(verbose_name='내용')
#     created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
#     modified_on = models.DateTimeField(auto_now=True)
#     post = models.ForeignKey(to='PersonalFaq', on_delete=models.CASCADE)   # 게시글 foreignKey 연결. 게시글이 삭제되면 댓글도 삭제되게 on_delete에 CASCADE 설정
#     writer = models.ForeignKey(to=User, on_delete=models.CASCADE) # 사용자 연결. 장고에서 만든 사용자 모델 연결
#     modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="PersonalComment.writer+", null=True, blank=True)
#     reference = models.ManyToManyField(to='PersonalFaq', related_name="PersonalFaq.head+", blank=True)



# 강사 코드

class Faq(models.Model):
    CATEGORY_CHOICES = [
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]

    # Field 타입은 한번 지정하면 안바꾸는게 좋음. 데이터가 들어가있는 상태에선 수정이 어렵고, 위험성 있음. 경험했지
    title = models.CharField(verbose_name='질문 제목', max_length=80)   # text field로 해도 되지만, character field가 더 적합함. 제목은 요약해서 적은 글씨로 쓰니까
    content = models.TextField(verbose_name='질문 내용')
    category = models.CharField(verbose_name='카테고리', max_length=2, choices = CATEGORY_CHOICES)

    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=model.CASCADE, related_name='faq_created_by')
    updated_by = models.ForeignKey(to=User, on_delete=model.CASCADE, related_name='faq_updated_by')

class Inquiry(models.Model):
    pass

class Answer(models.Model):
    pass