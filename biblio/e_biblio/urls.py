from django.conf.urls import include, url

from biblio import settings

urlpatterns = [
    url(r'^$', 'e_biblio.views.index'),
    url(r'add/', 'e_biblio.views.add_document'),
    url(r'thanks/', 'e_biblio.views.thanks'),
    #url(r'(?P<filename>\w+)', 'e_biblio.views.give_file')
]

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()