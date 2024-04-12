from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.filter(is_active=True, quantity__gt=0).values()
    return JsonResponse({'products': list(products)})