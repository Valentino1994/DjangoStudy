from django.db import models

# Create your models here.
class Article(models.Model):
    # Django는 pk는 알아서 만들어줌
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 생성일은 auto_now_add | 수정일은 auto_now
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)