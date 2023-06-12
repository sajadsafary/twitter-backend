from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        _("email"),
        unique=True,
        null=False,
        blank=False
    )

    joined_at = models.DateField(_('joined date'), auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.get_username()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    born_at = models.DateField(
        _('birth date'),
        default=None,
        null=True,
        blank=True
    )

    # image = models.ImageField(
    #     _('Image'),
    #     upload_to=f'user-{user}/profile/',
    #     blank=True,
    #     null=True
    # )

    def __str__(self):
        return f'{self.user} Profile'

