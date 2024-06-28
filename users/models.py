from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя с наследованием от AbstractUser, исключением поля username
    и переопределением USERNAME_FIELD на поле email.
    """

    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь ({self.email})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
