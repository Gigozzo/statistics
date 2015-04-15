from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import StatisticsView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', StatisticsView.as_view(), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
)
