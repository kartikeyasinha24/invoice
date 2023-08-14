# define a endpoint through which user can generate token 
# urls.py 
from rest_framework.routers import DefaultRouter
from inv_api import viewsets
router = DefaultRouter()
from django.urls.conf import  path,include
from django.contrib import admin
# register viewset with router
from rest_framework.authtoken.views import obtain_auth_token
router.register(r"invoice", viewsets.invoiceViewSet, basename="invoice")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-sauth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', obtain_auth_token)               
                     
]