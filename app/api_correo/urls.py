from django.urls import include,path
from api_correo.views import api_correoViewSet

 
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()
router.register(r'mail',api_correoViewSet,basename='api_correo')

urlpatterns = [ 
     path('',include(router.urls))
]