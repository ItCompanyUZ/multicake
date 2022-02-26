from modeltranslation.translator import translator, TranslationOptions
from . import models

class CakeTranslationOptions(TranslationOptions):
    fields = ('name',)


class CakeTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(models.Cake, CakeTranslationOptions)
translator.register(models.CakeType, CakeTypeTranslationOptions)


