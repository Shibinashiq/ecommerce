
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('category/', include('category.urls')),
    path('Brand/', include('brand.urls', namespace='brand')),
    path('product/', include('product.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)