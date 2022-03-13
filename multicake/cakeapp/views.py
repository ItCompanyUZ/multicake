from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import TemplateView

from . import models
from django.views import generic
from django.http import JsonResponse

from .models import Filling, Portfolio, Cake, CakeType


class MainView(generic.TemplateView):

    template_name = 'index.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['fillings'] = Filling.objects.all().order_by('-id')[0:3]
        context['portfolio'] = Portfolio.objects.all().order_by('-id')[0:6]
        context['total_fillings'] = Filling.objects.count()
        context['total_portfolio'] = Portfolio.objects.count()
        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['banner'] = models.Banner.objects.all().order_by('-id')

        return context


class ProductListView(TemplateView):
    paginate_by = 2
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cakeproduct'] = Cake.objects.filter(type__id = self.kwargs['pk'])
        context['caketype'] = CakeType.objects.get(id=self.kwargs['pk'])
        context['caketypes'] = CakeType.objects.all()
        return context





def load_more(request):
    if request.GET.get('offset'):
        offset = request.GET.get('offset')
        offset_int = int(offset)
        limit = 2
        fillings = list(Filling.objects.values().order_by('-id')[offset_int:offset_int+limit])

        for filling in fillings:
            filling['image'] = settings.MEDIA_URL + str(filling['image'])
            print(filling['image'])

        data = {
            'fillings': fillings
        }

    else:
        limit = 3
        offsetPort = request.GET.get('offset-portfolio')
        offsetPort_int = int(offsetPort)
        portfolio = list(Portfolio.objects.values().order_by('-id')[offsetPort_int:offsetPort_int+limit])

        for port in portfolio:
            port['image'] = settings.MEDIA_URL + str(port['image'])
            print(port['image'])

        data = {
            'portfolio': portfolio
        }

    
    return JsonResponse(data=data)



class DeliveryView(TemplateView):
    template_name = "delivery.html"



class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = "nmaaa"
        return context





