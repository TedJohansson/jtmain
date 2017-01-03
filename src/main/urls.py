from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserHomeView.as_view(), name='user_home'),
]
