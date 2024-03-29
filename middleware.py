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

from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

class AuthMiddleware(object):
    def process_request(self, request):
        if request.user.is_anonymous():
            if request.POST:
                login(request)
                if 'next' in request.GET:
                    # If user is redirected to login from an internal page
                    # redirect there after login
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    # Otherwise default going to root
                    return HttpResponseRedirect('/')
            elif request.path != '/login':
                return HttpResponseRedirect('%s?next=%s' % ('/login', request.path))
