from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_app import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset, base_name='user-detail')
router.register(r'groups', views.GroupViewset, base_name='group-detail')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
