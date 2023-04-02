from django.shortcuts import render
# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
# Create your views here.

from django.http import JsonResponse
from products.models import Product

from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
   serializer = ProductSerializer(data = request.data)
   output_data = {}
   if serializer.is_valid():
      instance = serializer.save()
      output_data  = serializer.data
      print(instance)
      return Response(output_data)
   else:
      print(serializer.data)
      return Response({"text" : "could not load"})
#    instance = Product.objects.get(id=1)
#    output_data = {}
#    if instance:
#       output_data = ProductSerializer(instance).data

    

