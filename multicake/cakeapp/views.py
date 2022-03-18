from django.core.paginator import Paginator
from django.views.generic import ListView
from multiprocessing import context
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.generic import TemplateView
from . import forms
from . import models
from django.views import generic
from django.http import JsonResponse

from .forms import OrderForm
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


class PortfolioView(generic.TemplateView):

    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.all().order_by('-id')[0:6]
        context['total_portfolio'] = Portfolio.objects.count()

        return context


class FillingView(generic.TemplateView):

    template_name = 'filling.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['fillings'] = Filling.objects.all().order_by('-id')[0:3]
        context['total_fillings'] = Filling.objects.count()

        return context


class ProductListView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        product = Cake.objects.filter(type__id = self.kwargs['pk'])[::-1]
        product_paginator = Paginator(product, 2)
        page_number = self.request.GET.get('page')
        context = super().get_context_data(**kwargs)
        context['cakeproduct'] = product_paginator.get_page(page_number)
        context['caketype'] = CakeType.objects.get(id=self.kwargs['pk'])
        context['caketypes'] = CakeType.objects.all()

        return context


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Cake
    form_class = forms.OrderForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cake'] = Cake.objects.get(id = self.kwargs['pk'])
        context['caketype_id'] = context['cake'].type.id
        context['fillings'] = Filling.objects.all()
        form = forms.OrderForm(self.request.POST or None)

        context["form"] = form

        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        print(request.POST)
        print(context["form"])

        if context["form"].is_valid():
            print("Succcessss")
            context["form"].save()

            return redirect('/')
        else:
            form = OrderForm()
            return render(request, 'product_detail.html', {'form': form})



    



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


class CantactView(TemplateView):
    template_name = "map.html"


class DeliveryView(TemplateView):
    template_name = "delivery.html"




class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = "nmaaa"
        return context





