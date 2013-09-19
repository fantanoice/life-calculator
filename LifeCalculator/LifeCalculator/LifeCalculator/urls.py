from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^LifeCalc/', include('LifeCalc.urls')),
  url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
  from django.contrib.staticfules.urls import staticfiles_urlpatterns
  urlpatterns += staticfiles_urlpatterns()