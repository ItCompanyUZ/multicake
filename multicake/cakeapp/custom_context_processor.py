from .models import Logo, Contact


def logo(request):
    return {
       'logo': Logo.objects.first(),
    }


def cantact(request):
    return {
        'cantact': Contact.objects.all()
    }