from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cake(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)
