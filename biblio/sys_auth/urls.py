from django.conf.urls import include, url
from sys_auth import views

urlpatterns = [
    url(r'login/', views.LoginFormView.as_view()),
]
