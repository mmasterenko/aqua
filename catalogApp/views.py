from utils import group_list
from django.shortcuts import render
from .models import Catalog


def categories(req):
    context = {
        'category_rows': group_list(Catalog.objects.all(), 3),
        'title': 'Aqua'
    }
    return render(req, 'catalogApp/portfolio-3-col.html', context=context)
