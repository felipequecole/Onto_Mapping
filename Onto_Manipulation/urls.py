from django.conf.urls import url
from Onto_Manipulation import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^convert/$', views.convert, name='convert'),
    url(r'^download/$', views.download, name='download'),
]
