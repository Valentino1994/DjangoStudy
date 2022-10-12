from django.contrib import admin
from .models import Article

# Register your models here.
# Admin 화면을 커스텀할 수 있음
class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'updated_at', 'created_at')

# admin site에 Article을 register하겠다.
admin.site.register(Article, ArticleAdmin)
