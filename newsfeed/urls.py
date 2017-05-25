from django.conf.urls import url

from . import views

app_name = 'headlines'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^bbcnews$', views.bbcnews, name='bbcnews'),
	url(r'^cnn$', views.cnn, name='cnn'),
]