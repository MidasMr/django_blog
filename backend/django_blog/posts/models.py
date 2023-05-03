from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст поста'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        null=True,
        blank=True
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    STR_TEXT = (
        'Текст: {text:15}, '
        'Автор: {username}, '
        'Дата: {pub_date}'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.STR_TEXT.format(
            text=self.text,
            username=self.author.username,
            pub_date=self.pub_date
        )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='Пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    STR_TEXT = (
        'Текст: {text:15}, '
        'Автор: {author}, Пост: {post}, '
        'Дата: {created}'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.STR_TEXT.format(
            text=self.text,
            author=self.author.username,
            post=self.post,
            created=self.created
        )
