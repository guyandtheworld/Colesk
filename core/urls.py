from django.conf.urls import url
from . import views

urlpatterns = [ url('^$', views.main_page, name = 'main_page'),
				url('^home/$', views.home, name = 'home'),
				url('^you/$',views.you, name = 'you'),
			]