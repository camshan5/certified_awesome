from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    PROFESSIONS = (
        ("rn", "Registered Nurse"),
        ("np", "Nurse Practioner"),
        ("other", "Other"),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    profession = CharField(
        _("Select Profession"), blank=True, max_length=25, choices=PROFESSIONS
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
