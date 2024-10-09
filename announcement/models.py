from django.db import models

from user.models import User

NULLABLE = {"null": True, "blank": True}


class Announcement(models.Model):

    title = models.CharField(max_length=150, verbose_name="название товара")
    price = models.IntegerField(verbose_name="цена товара")
    description = models.TextField(verbose_name="описание товара")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь, который создал объявление",
        **NULLABLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="время и дата создания объявления", **NULLABLE
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "объявление"
        verbose_name_plural = "объявления"

    def __str__(self):
        return self.title


class Feedback(models.Model):
    text = models.TextField(verbose_name="текст отзыва")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="пользователь, который оставил отзыв",
        **NULLABLE
    )
    ad = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        verbose_name=" объявление, под которым оставлен отзыв",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="время и дата создания отзыва", **NULLABLE
    )

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    def __str__(self):
        return self.text
