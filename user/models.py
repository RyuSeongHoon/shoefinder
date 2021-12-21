from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name="유저 아이디")
    user_pw = models.CharField(max_length=128, verbose_name="유저 비밀번호")
    user_name = models.CharField(max_length=16, verbose_name="유저 이름")
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="계정 생성시간")
    
    def __str__(self):
        return self.user_name

    class Meta: # DB테이블명을 지정해주는 옵션
        db_table = 'users' # 테이블명
        verbose_name = '유저' # 테이블의 닉네임
        verbose_name_plural = '유저'