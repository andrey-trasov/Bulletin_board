from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="электронная почта")
    first_name = models.CharField(max_length=50, verbose_name="имя пользователя")
    last_name = models.CharField(max_length=50, verbose_name="фамилия пользователя")
    phone = models.CharField(max_length=20, verbose_name="телефон для связи")

    Roles  = [
        ("user", "пользователь"),
        ("admin", "администратор")
    ]

    role  = models.CharField(max_length=20, verbose_name="роль пользователя", choices=Roles)
    image = models.ImageField(upload_to="product/photo", verbose_name="аватарка пользоавателя", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email



