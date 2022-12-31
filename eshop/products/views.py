from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect , HttpResponse

from products.models import Product , SizeVariant
from accounts.models import Cart , CartItems , Profile 
# Create your views here.


def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product' : product}

        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(5)
        print(6) 
        return render(request, 'product/product.html', context = context)
    except Exception as e:
        print(e)



