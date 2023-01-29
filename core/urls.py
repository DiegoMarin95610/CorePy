from django.contrib import admin
from django.urls import path, re_path, include

from django.views.generic import TemplateView
from django.conf.urls.static  import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#^ afirma la posición al principio de una línea
# . coincide con cualquier carácter (excepto terminadores de línea)
# * coincide con el token anterior entre cero e ilimitadas veces, tantas veces como sea posible, devolviendo lo necesario
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]