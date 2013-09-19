from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^LifeCalc/', include('LifeCalc.urls')),
  # Examples:
  #url(r'^$', 'LifeCalculator.views.home', name='home'),
  #url(r'^LifeCalculator/', include('LifeCalculator.LifeCalculator.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
  from django.contrib.staticfules.urls import staticfiles_urlpatterns
  urlpatterns += staticfiles_urlpatterns()