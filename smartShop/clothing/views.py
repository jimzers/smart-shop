from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Clothing
# Create your views here.

def index(request):
    all_clothings = Clothing.objects.all()
    context = {'all_clothings': all_clothings}
    return render(request, 'clothingTemplates/index.html', context)

def detail(request, clothing_id):
    try:
        clothing = Clothing.objects.get(pk=clothing_id)
    except Clothing.DoesNotExist:
        raise Http404('Clothing does not exist')
    return render(request, 'clothingTemplates/detail.html', {'clothing': clothing})
