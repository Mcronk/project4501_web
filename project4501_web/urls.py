from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project4501_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    #url(r'^/(?P<pk>[0-9]+)/$', views.index, name='index'),
    url(r'^product/$', views.product, name='product'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product, name='product'),
)
