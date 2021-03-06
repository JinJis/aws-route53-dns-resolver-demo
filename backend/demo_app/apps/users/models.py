from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from .managers import UserManager


class User(AbstractUser):
    """Default user for L&D Investment Platform."""

    #: First and last name do not cover name patterns around the globe
    email = models.EmailField(unique=True)

    objects = UserManager()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("api:users:user-detail", kwargs={"user_id": self.id})
