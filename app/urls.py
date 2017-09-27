from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^create/$', views.Create.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.Delete.as_view(), name='delete'),
    url(r'^copy/(?P<pk>[0-9]+)/$', views.Copy.as_view(), name='copy'),
]
