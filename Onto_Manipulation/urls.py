from django.conf.urls import url
from Onto_Manipulation import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^relation/$', views.relation, name='relation'),
    url(r'^category/$', views.category, name='category'),
    url(r'^edit/(?P<id>\w+)/$', views.select, name='edit'),
    url(r'^edit_cat/(?P<id>\w+)/$', views.edit_cat, name='edit_cat'),
    url(r'^edit_rel/(?P<id>\w+)/$', views.edit_rel, name='edit_rel'),
    url(r'^convert/$', views.convert, name='convert'),
    url(r'^download/$', views.download, name='download'),
    url(r'^download_xml/$', views.download_XML, name='download'),
    url(r'^download_xls/$', views.download_XLS, name='download'),
    url(r'^upload_xml/$', views.upload_XML, name='upload'),
    url(r'^upload_xls/$', views.upload_XLS, name='upload'),
]
