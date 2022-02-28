from distutils.command.upload import upload
from tabnanny import verbose
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
    image = models.ImageField(_('Rasm'), upload_to='To\'rtlar')


    class  Meta:
        verbose_name = 'To\'rt'
        verbose_name_plural = 'To\'rtlar'

    def __str__(self) -> str:
        return self.name



class Filling(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)
    composition = models.CharField(_('Tarkibi'), max_length=255)
    image = models.ImageField(_('Rasm'),blank=True, null=True, upload_to='Nachinka')


    class Meta:
        verbose_name = 'Nachinka'
        verbose_name_plural = 'Nachinkalar'


    def __str__(self) -> str:
        return self.name

    
class Portfolio(models.Model):
    image = models.ImageField(_('Rasm'), upload_to='Biznig ishlar')


    class Meta:
        verbose_name = 'Bizning ish'
        verbose_name_plural = 'Bizning ishlar'

    

