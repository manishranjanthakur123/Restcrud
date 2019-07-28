from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.toy_list, name='get_toys'),
    url(r'^(?P<pk>[0-9]+)$', views.toy_detail, name='toys_detail'),
]