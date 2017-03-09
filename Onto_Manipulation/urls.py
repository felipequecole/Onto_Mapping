from django.conf.urls import url
from Onto_Manipulation import views

urlpatterns = [
    url(r'^$', views.relation, name='index'),
    url(r'^relation/$', views.relation, name='relation'),
    url(r'^category/$', views.category, name='category'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^convert/$', views.convert, name='convert'),
    url(r'^download/$', views.download, name='download'),
]
