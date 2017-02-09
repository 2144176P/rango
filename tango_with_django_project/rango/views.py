from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category

def index(request):

    category_list = Category.objects.orger_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # NB the first parameter is the template we wish to use i.e rango/index.html
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    return render(request, 'rango/about.html')