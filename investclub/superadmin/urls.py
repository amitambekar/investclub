from django.conf.urls import include, url
from superadmin.views import home 

urlpatterns = [
    url(r'^$', home.index),
	url(r'homepage/$', home.homepage),
	
	]


