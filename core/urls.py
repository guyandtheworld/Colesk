from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.main_page, name = 'main_page'),
    			url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
				url(r'^new/$', views.new_post, name = 'new_post'),
				url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
			]					