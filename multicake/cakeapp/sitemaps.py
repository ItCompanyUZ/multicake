from django.contrib.sitemaps import Sitemap
from .models import Cake, Filling


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Cake.objects.all()

    def lastmod(self, obj):
        return obj.updated


class FillingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Filling.objects.all()

    def lastmod(self, obj):
        return obj.updated
