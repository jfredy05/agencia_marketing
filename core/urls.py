from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.urls import path, re_path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("api/blog/", include('apps.blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
