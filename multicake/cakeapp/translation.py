from modeltranslation.translator import translator, TranslationOptions
from . import models

class CakeTranslationOptions(TranslationOptions):
    fields = ('name',)


class CantactTranslationOptions(TranslationOptions):
    fields = ('adress',)


class CakeTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class FillingTranslationOptions(TranslationOptions):
    fields = ('name', 'composition',)

translator.register(models.Cake, CakeTranslationOptions)
translator.register(models.CakeType, CakeTypeTranslationOptions)
translator.register(models.Filling, FillingTranslationOptions)
translator.register(models.Contact, CantactTranslationOptions)

