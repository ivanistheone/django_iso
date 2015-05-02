from django.conf.urls import patterns, url

urlpatterns = patterns('djangosite.views',
    url(r'^$', 'index', name='index'),
)