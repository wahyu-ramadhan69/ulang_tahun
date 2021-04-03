from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('brithday.urls')),
    url(r'^brithday/', include('brithday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
