from django.shortcuts import render

# def products(request):
#     links_menu = {'links': [
#         {'href': 'index', 'name': 'все'},
#         {'href': 'index', 'name': 'дом'},
#         {'href': 'index', 'name': 'офис'},
#         {'href': 'index', 'name': 'модерн'},
#         {'href': 'index', 'name': 'классика'},
#     ]}
#     return render(request, 'products.html', context=links_menu)


from django.shortcuts import render
from mainapp.models import Product, ProductCategory

def categories(request):
    categories = ProductCategory.objects.all()

    context = {
        'categories': categories,
        'href': 'products:index'
    }
    return render(request, 'products.html', context=context)