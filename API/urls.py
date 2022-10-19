from rest_framework import routers
from .views import *
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'posts', PostViewset)


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]