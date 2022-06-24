from django.contrib import admin

from .models import Article, Sections, ArticleSection
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


# class ArticleSectionInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         count = 0
#         for form in self.forms:
#             if form.cleaned_data.get('status'):
#                 count += 1
#         if count == 0:
#             raise ValidationError('Укажите основной раздел')
#         elif count > 1:
#             raise ValidationError('Основным может быть только один раздел')
#         return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 5
    # formset = ArticleSectionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']


@admin.register(Sections)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [ArticleSectionInline, ]

