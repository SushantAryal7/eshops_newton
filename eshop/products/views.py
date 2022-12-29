from django.shortcuts import render
from products.models import Product 
# Create your views here.


def get_product(request, slug):
    print('1')
    try:
        print('2')
        product = Product.objects.get(slug=slug)
        print(3)
        context = {'product' : product}
        print('4')

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
