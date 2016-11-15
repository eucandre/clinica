from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app_clinica.views import *
from estoque.views import *
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'dentista', DentistaViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'funcionario', FuncionarioViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',view=inicia),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
