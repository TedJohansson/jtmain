from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_to_app, name='login'),
    url(r'^login_to_app/$', views.login_to_app, name='login_to_app'),
    url(r'^logout/$', views.logout_of_app, name='logout_of_app'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='update_user'),
    url(r'^$', views.UserHomeView.as_view(), name='user_home'),
    url(r'^new_post/$', views.AddPostView.as_view(), name='add_post'),
]
