from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.main_page, name = 'main_page'),
    			url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
				url(r'^home/$', views.home, name = 'home'),
				url(r'^you/$',views.you, name = 'you'),
			]