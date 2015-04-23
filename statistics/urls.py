from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView
from main.views import spam, total, reverts, complaints

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
                       url('^spam/?$', spam, name='spam'),
                       url('^total/?$', total, name='total'),
                       url('^reverts/?$', reverts, name='reverts'),
                       url('^complaints/?$', complaints, name='complaints'),
                       url(r'^$', TemplateView.as_view(template_name='statistics.html')),
                       url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
