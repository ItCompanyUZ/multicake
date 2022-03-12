from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView

from . import models
from django.views import generic
from django.http import JsonResponse

from .models import Filling, Portfolio, Cake, Logo, CakeType


class MainView(generic.TemplateView):

    template_name = 'index.html'


    def get_context_data(self, **kwargs):


        filling = Filling.objects.all()[::-1]
        portfolio = Portfolio.objects.all()[::-1]

        filling_paginator = Paginator(filling, 3)
        page_number = self.request.GET.get('page')

        portfolio_paginator = Paginator(portfolio, 3)
        page_portfolio = self.request.GET.get('page')


        context = super().get_context_data(**kwargs)
        context['fillings'] = filling_paginator.get_page(page_number)
        context['posts'] = Filling.objects.all().order_by('-id')[0:3]
        context['total_obj'] = Filling.objects.count()
        context['portfolio'] = portfolio_paginator.get_page(page_portfolio)
        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['banner'] = models.Banner.objects.all().order_by('-id')

        return context


# def productcake(request, id):
#     tort = CakeType.objects.filter(cake=id)
#     paginator = Paginator(tort, 6)
#     page = request.GET.get('page')
#     cakeproduct = paginator.get_page(page)
#     return render(request, 'product.html', {'cakeproduct': cakeproduct})


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
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    post_obj = list(Filling.objects.values().order_by('-id')[offset_int:offset_int+limit])
    for post in post_obj:
        post['image'] = settings.MEDIA_URL + str(post['image'])

    data = {
        'posts': post_obj
    }
    return JsonResponse(data=data)

# get(id = self.kwargs['pk'])

# class ProductListView(generic.DetailView):
#     template_name = 'product.html'
#     model = Cake
#
#     def get_context_data(self, request, pk, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(pk)
#         return render(request, 'product.html')



class DeliveryView(TemplateView):
    template_name = "delivery.html"



class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = "nmaaa"
        return context





# class JsonListView(View):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         upper = kwargs.get('num_fillings')
#         lower = upper-3
#         size = len(models.Filling.objects.all())
#         max_size = True if upper >= size else False
#         print(upper)
#         fillings = list(models.Filling.objects.values()[lower:upper])
#         return JsonResponse({'data': fillings, 'max': max_size}, safe=False)

def main(request):
    return render(request, 'index.html')



