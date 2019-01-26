from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf import settings
from blog.sitemaps import PostSiteMap

sitemaps = {
    'posts': PostSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('registration/', include('registration.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^sitemap\.xml$',sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)