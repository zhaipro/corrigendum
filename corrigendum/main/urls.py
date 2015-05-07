from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit_form/$', views.edit_form, name='edit_form'),
	url(r'^save', views.save, name='save'),
    url(r'^add_book_form/$', views.add_book_form, name='add_book_form'),
	url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^(?P<pk>[0-9]+)/history/$', views.history, name='history'),
	url(r'^search/$', views.search, name='search'),
]
