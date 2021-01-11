from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from login.models import Customer
from login.serializers import CustomerSerializer


@csrf_exempt
@api_view(["POST"])
def customer_login(request, format=None):
    """
    Validates customer pin_code.
    """
    pin_code = request.POST.get("pin_code", "")
    if len(pin_code) != 5:
        # todo validation response about pin length
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = Customer.objects.get(pin_code=pin_code)
    except (KeyError, Customer.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """

    queryset = Customer.objects.all().order_by("-date_joined")
    serializer_class = CustomerSerializer
    # disable auth
    # permission_classes = [permissions.IsAuthenticated]
