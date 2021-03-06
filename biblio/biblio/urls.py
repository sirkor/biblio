from django.conf.urls import include, url
from django.contrib import admin
import e_biblio.urls
import sys_auth.urls
import sys_auth.views
urlpatterns = [
    # Examples:
    # url(r'^$', 'biblio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', sys_auth.views.LoginFormView.as_view()),
    url(r'auth/', include(sys_auth.urls)),
    url(r'', include(e_biblio.urls)),
]
