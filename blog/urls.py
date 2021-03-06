from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_lists'),
	url(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post_detail/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	]
