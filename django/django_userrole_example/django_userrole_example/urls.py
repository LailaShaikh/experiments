from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_userrole_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', 'myuser.views.home', name='home'),
    url(r'^s/$', 'myuser.views.customize_page_style', name='customize'),
    url(r'^admin/', include(admin.site.urls)),

)
