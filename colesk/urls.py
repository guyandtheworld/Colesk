from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from colesk.core import views as core_views
from colesk.accounts import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name = 'home'),
    url(r'^signup/$', account_views.signup, name = 'signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/cover.html'}, name = 'login'),
    url(r'^logout/$', auth_views.logout, name = 'logout')

]
