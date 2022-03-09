from django.core.paginator import Paginator
from django.shortcuts import render
from . import models
from django.views import View, generic
from django.http import JsonResponse

from .models import Filling


class PublisherDetailView(generic.TemplateView):

    template_name = 'index.html'


    def get_context_data(self, **kwargs):


        filling = Filling.objects.all()[::-1]

        filling_paginator = Paginator(filling, 3)
        page_number = self.request.GET.get('page')


        context = super().get_context_data(**kwargs)
        context['fillings'] = filling_paginator.get_page(page_number)
        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['portfolio'] = models.Portfolio.objects.all().order_by('-id')[:9]
        context['banner'] = models.Banner.objects.all().order_by('-id')

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



