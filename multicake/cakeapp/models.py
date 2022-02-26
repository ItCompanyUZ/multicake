from django.db import models
from django.utils.translation import ugettext_lazy as _


class CakeType(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)

    class Meta:
        verbose_name = 'To\'rt turi'
        verbose_name_plural = 'To\'rt turlari'

    def __str__(self) -> str:
        return self.name



class Cake(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)  
    type = models.ForeignKey(CakeType, on_delete=models.CASCADE, verbose_name=_('Turi'))
    price_for_kg = models.FloatField(_('1 kg narxi'))
    min_amount_kg = models.PositiveIntegerField(_('Eng kam buyurtma miqdori (kg)'))


    class  Meta:
        verbose_name = 'To\'rt'
        verbose_name_plural = 'To\'rtlar'

    def __str__(self) -> str:
        return self.name


