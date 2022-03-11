from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from . import models
from django.views import generic

from .models import Filling, Portfolio, Cake, Logo


class PublisherDetailView(generic.TemplateView):

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
        context['portfolio'] = portfolio_paginator.get_page(page_portfolio)
        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['banner'] = models.Banner.objects.all().order_by('-id')

        return context


def productcake(request, pk):
    tort = Cake.objects.filter(caketype=pk)
    paginator = Paginator(tort, 6)
    page = request.GET.get('page')
    cakeproduct = paginator.get_page(page)
    return render(request, 'product.html', {'cakeproduct': cakeproduct})


class ProductListView(generic.DetailView):
    template_name = 'product.html'
    model = Cake

    def get_context_data(self, request, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        print(pk)
        return render(request, 'product.html')







class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.all()
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



