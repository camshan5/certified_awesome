from django.db import models
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class Certs(models.Model):

    name = CharField(_("Name of User"), blank=True, max_length=255)
    cert_id = CharField(_("Certification ID"), blank=True, max_length=255)
