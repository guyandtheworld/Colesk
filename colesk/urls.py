from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve as static_view

from colesk.core import views as core_views
from colesk.accounts import views as account_views
from colesk.feeds import views as feed_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico/$', static_view, {'path': 'colesk/static/'}),
    url(r'^$', core_views.home, name = 'home'),
    url(r'^signup/$', account_views.signup, name = 'signup'),
    url(r'^login/$', account_views.login, name = 'login'),
    url(r'^logout/$', account_views.logout, name = 'logout'),
    url(r'^new-question/$', feed_views.new_question, name='new_question'),
    url(r'^(?P<pk>[\w-]+)/$', feed_views.question_detail, name = 'question_detail'),
]
