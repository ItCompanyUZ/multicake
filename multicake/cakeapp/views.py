from re import S
from this import d
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.generic import TemplateView
from . import forms
from . import models
from django.views import generic
from django.http import JsonResponse
import telegram_send

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


class ProductFilterView(generic.TemplateView):

    template_name = 'product_filter.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]

        return context


class PortfolioView(generic.TemplateView):

    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.all().order_by('-id')[0:3]
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
        
        context = super().get_context_data(**kwargs)
        context['cakeproduct'] = Cake.objects.filter(type__id = self.kwargs['pk']).order_by('-id')[0:3]
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

        if context["form"].is_valid():
            context["form"].save()
            filling_id = context['form']['filling'].value()
            cake_id = context['form']['cake'].value()
            delivery_id = context['form']['type_of_delivery'].value()

            filling = models.Filling.objects.get(id=filling_id)
            cake = models.Cake.objects.get(id=cake_id)
            caketype = cake.type

            if int(delivery_id) == 1:
                delivery = 'Olib ketish'
            else:
                delivery = 'Yetkazib berish'


            array = [f"Sizga yangi buyurtma kelib tushdi:✅ \n\n🎂To'rtning turi: {caketype.name} \n🎂To'rt nomi: {cake.name} \n📅Kuni:  {context['form']['date'].value()} \n📞Buyurtmachi raqami:  {context['form']['number'].value()} \n⚖️Necha kg:  {context['form']['how_many_kg'].value()} \n🍰Nachinka:  {filling.name} \n📝To\'rt ustiga yozuv: {context['form']['writing'].value()} \n🚕Yetkazish turi:  {delivery}"]


            telegram_send.send(messages=array)


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

    elif request.GET.get('offset-4'):
        offset = request.GET.get('offset-4')
        offset_int = int(offset)
        limit = 4
        fillings = list(Filling.objects.values().order_by('-id')[offset_int:offset_int+limit])

        for filling in fillings:
            filling['image'] = settings.MEDIA_URL + str(filling['image'])
            print(filling['image'])

        data = {
            'fillings': fillings
        }

    elif request.GET.get('offset-product'):
        offset = request.GET.get('offset-product')
        offset_int = int(offset)
        limit = 1
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








