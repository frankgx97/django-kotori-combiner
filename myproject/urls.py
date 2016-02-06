# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from djago.views.generic import RedirectView

urlpatterns = patterns('',
	#(r'^app/', include('myproject.myapp.urls')),
	#(r'^$', RedirectView.as_view(url='/app/gen/')), # Just for ease of use.
	url(r'^$', 'myproject.myapp.views.list', name='list'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
