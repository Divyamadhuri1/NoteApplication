from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addnote', views.addnote, name='addnote'),
    url(r'^updatenote', views.updatenote, name = 'updatenote'),
    url(r'^deletenote', views.deletenote, name= 'deletenote'),
    url(r'^getallnotes', views.getallnotes, name= 'getallnotes')
    ]

