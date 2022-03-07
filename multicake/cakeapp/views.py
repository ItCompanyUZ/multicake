from django.shortcuts import render
from . import models
from django.views import generic


 



class PublisherDetailView(generic.TemplateView):

    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['fillings'] = models.Filling.objects.all().order_by('-id')[:4]
        context['portfolio'] = models.Portfolio.objects.all().order_by('-id')[:9]

        return context











def main(request):
    return render(request, 'index.html')



