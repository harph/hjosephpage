from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'web.views.index'),
)