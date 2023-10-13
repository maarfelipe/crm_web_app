from django.shortcuts import render

from .models import Lead


def home_page(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'home_page.html', context)

