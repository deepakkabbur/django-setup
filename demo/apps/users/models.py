from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"), unique=True, blank=False, max_length=254, validators=[]
    )

    active = models.BooleanField(_("active"), default=False, help_text=_("Active user"))

    first_name = models.CharField(_("First Name"), max_length=254, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=254, blank=True)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
            "Unselect this instead of deleting accounts."
        ),
    )
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "users"
        ordering = ["-date_created", "email"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["first_name", "last_name"]),
        ]
