from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response 
from . models import *

# Create your views here.
def fn_Course(request):
    return render(request,'search.html')

@api_view(['POST'])
def fn_saveCourse(request):
    productName = request.data
    product = Product(prodctname = productName['name'])
    product.save()
    if product.id >0:
        return Response('product saved')
    else:
        return Response('failed')
    

@api_view(['GET'])
def fn_showProduct(request):
    key = request.GET['letter']
    print(key)
    product_list = []
    try:
        products = Product.objects.filter(prodctname__istartswith=key)
        print(products.query)
        if products:
            for product in products:
                product_list.append(product.prodctname)
            return Response(product_list)
        return Response('no matching details')
    except:
        return Response('faild try again')


