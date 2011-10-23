#coding=utf8
'''
    This file is part of Fotos
    Copyright 2011 Halfdan Mouritzen

    Fotos is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    Fotos is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Fotos.  If not, see <http://www.gnu.org/licenses/>.
'''

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.upload.models import *
from apps.upload.views import *

urlpatterns = patterns('',
    (r'^$', frontpage),
    (r'^stream$', overview, {'stream':True}),
    (r'^overview$', overview),

    (r'^upload', upload),

    (r'^login', login_view),
    (r'^logout', logout_view),

    # Don't use this in a production environment
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
