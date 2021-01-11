# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from login.models import Customer
from login.serializers import CustomerSerializer
# from rest_framework.mixins import (
#     CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
# )
# from rest_framework.viewsets import GenericViewSet


@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request, format=None):
    """
    List all customers, or create a new customer.
    """
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print('kerem', request.POST)
        print('kerem', request.data.get('pin_code'))
        try:
            customer = Customer.objects.get(
                pin_code=request.data.get('pin_code'))
        except (KeyError, Customer.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    """
    Retrieve, update or delete a code customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET'])
def customer_login(request, pin_code):
    """
    Retrieve, update or delete a code customer.
    """
    try:
        customer = Customer.objects.get(pin_code=pin_code)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'PUT':
    #     serializer = CustomerSerializer(customer, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     customer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer
    # disable auth
    # permission_classes = [permissions.IsAuthenticated]
