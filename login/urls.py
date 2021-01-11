from django.urls import include, path

from . import views
# from django.conf.urls import patterns, url
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('customers_list/', views.customer_list),
    # path('customers/<int:pk>/', views.customer_detail),
    # path('api/customers/', views.customer_list),
    path('api/customer_login/', views.customer_list)
]
# url(r'^api/v1/customers/(?P<slug>[0-9]+)$', 'customer_detail')

# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
