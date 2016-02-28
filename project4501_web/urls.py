from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project4501_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^course/$', views.course_info, name='course_info'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_info, name='course_info'),
    url(r'^courseList/$', views.courseList, name='courseList'),

) 

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)