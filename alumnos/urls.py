from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from api import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken

from django.conf import settings
from django.conf.urls.static import static

#Adding endpoints to viewsets
router = routers.DefaultRouter()
router.register('alumnos', views.AlumnoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    url('api/v1/detail/alumnos/(?P<pk>[0-9]+)/$', views.AlumnoEditDelete.as_view()),
    # ----------------------------------------------------------------------------------
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/',include('rest_auth.registration.urls')),
]


