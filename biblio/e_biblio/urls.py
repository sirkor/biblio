from django.conf.urls import include, url

from biblio import settings

urlpatterns = [
    url(r'^$', 'e_biblio.views.index'),
    url(r'thanks/', 'e_biblio.views.thanks'),
    url(r'add/', 'e_biblio.views.add_document'),
    url(r'delete/(?P<id>[0-9]+)', 'e_biblio.views.del_document'),
    url(r'update/(?P<id>[0-9]+)', 'e_biblio.views.update_view'),
    url(r'search/', 'e_biblio.views.search_view'),
]

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()