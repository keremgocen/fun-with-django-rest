from django.urls import include, path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"customers", views.CustomerViewSet)

# todo display customer_login in api-root

urlpatterns = [
    path("", include(router.urls)),
    path("api/customer_login/", views.customer_login),
]
