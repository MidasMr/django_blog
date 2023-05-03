from django.contrib.admin import ModelAdmin, register

from .models import Post, Comment


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'pub_date',
        'author',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = (
        'text',
        'author',
    )
    search_fields = ('text',)
    empty_value_display = '-пусто-'
