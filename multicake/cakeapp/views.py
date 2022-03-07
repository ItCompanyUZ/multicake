from django.shortcuts import render
from . import models
from django.views import View, generic
from django.http import JsonResponse


 



class PublisherDetailView(generic.TemplateView):

    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['cakes'] = models.CakeType.objects.all().order_by('-id')[:9]
        context['fillings'] = models.Filling.objects.all().order_by('-id')[:4]
        context['portfolio'] = models.Portfolio.objects.all().order_by('-id')[:9]

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



