from django.urls import include, path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers_list/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),
]
