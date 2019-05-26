from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<driver_id>[0-9]+)/$', views.driver_detail),
    url(r'^start/$', views.start)
]