from django.conf.urls import url
from django.contrib import admin

from colesk.core import views as core_views
from colesk.accounts import views as account_views
from colesk.feeds import views as feed_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name = 'home'),
    url(r'^signup/$', account_views.signup, name = 'signup'),
    url(r'^login/$', account_views.login, name = 'login'),
    url(r'^logout/$', account_views.logout, name = 'logout'),
    url(r'^(?P<title>[^/]+)/$', feed_views.question, name = 'question'),
    url(r'^new/$', feed_views.new, name='new_post'),

]
