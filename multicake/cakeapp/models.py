from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse




class Banner(models.Model):
    image = models.ImageField(_('Rasm'), upload_to='Banner')


    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Bannerlar'


class Logo(models.Model):
    image = models.ImageField(_('Rasm'), upload_to='Logo')


    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'



class CakeType(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)
    image = models.ImageField(_('Rasm'), upload_to='To\'rt turlari')

    class Meta:
        verbose_name = 'To\'rt turi'
        verbose_name_plural = 'To\'rt turlari'

    def __str__(self) -> str:
        return self.name



class Cake(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)  
    type = models.ForeignKey(CakeType, on_delete=models.CASCADE, verbose_name=_('Turi'))
    price_for_kg = models.CharField(_('1 kg narxi'), max_length=200)
    min_amount_kg = models.PositiveIntegerField(_('Eng kam buyurtma miqdori (kg)'))
    image = models.ImageField(_('Rasm'), upload_to='To\'rtlar')

    def get_absolute_url(self):
        return reverse("cakeapp:product", args=[self.id])

    class  Meta:
        verbose_name = 'To\'rt'
        verbose_name_plural = 'To\'rtlar'

    def __str__(self) -> str:
        return self.name


class Filling(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)
    composition = models.CharField(_('Tarkibi'), max_length=255)
    image = models.ImageField(_('Rasm'),blank=True, null=True, upload_to='Nachinka')

    def get_absolute_url(self):
        return reverse("cakeapp:fillings", args=[self.id])

    class Meta:
        verbose_name = 'Nachinka'
        verbose_name_plural = 'Nachinkalar'


    def __str__(self) -> str:
        return self.name

    
class Portfolio(models.Model):
    image = models.ImageField(_('Rasm'), upload_to='Biznig-ishlar')


    class Meta:
        verbose_name = 'Bizning ish'
        verbose_name_plural = 'Bizning ishlar'

    
class Contact(models.Model):
    number = models.CharField(_('Telefon raqam'), max_length=23)
    email = models.EmailField()
    adress = models.CharField(_('Joylashuv manzili'), max_length=250)
    status = models.BooleanField(_('Holati'), default=False)
    instagram = models.URLField(_('Instagram uchun link'),)
    telegram = models.URLField(_('Telegram uchun link'))


    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'


    def __str__(self) -> str:
        return str(self.number)


@receiver(pre_save, sender=Contact)
def my_handler(sender, instance=None, created=False, **kwargs):

    if str(instance)[0:4] != '+998' or len(str(instance)) < 13:
        raise ValueError(_("Raqam noto\'g\'ri kiritildi"))



class Order(models.Model):


    class DeliveryTypes(models.IntegerChoices):
        self_delivery = 1, _('Olib ketish')
        delivery = 2, _('Yetkazib berish')


    date = models.DateField(_('Qaysi kunga'))
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, verbose_name='To\'rt')
    number = models.CharField(_('Telefon raqam'), max_length=13)
    how_many_kg = models.PositiveIntegerField(_('Kerakli hajim (kg)'))
    filling = models.ForeignKey(Filling, on_delete=models.CASCADE, verbose_name='Nachinka')
    writing = models.CharField(_('To\'rt ustidagi yozuv'), max_length=255)
    type_of_delivery = models.PositiveIntegerField(_('Yetkazib berish turi'),  default=DeliveryTypes.self_delivery, choices=DeliveryTypes.choices)


    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'


    def __str__(self) -> str:
        return f'{self.number} -> {self.cake.name}  {self.date}'
