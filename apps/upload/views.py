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

from django.template import RequestContext, loader, Context
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth import logout

from models import *

from django.conf import settings

from uuid import uuid3, NAMESPACE_DNS

from django.core.files import File

def handle_uploaded_file(fileobj):
    ''' Handles a single file object being uploaded
    '''

    fileext = fileobj.name.rsplit('.')[1]
    uuidstr = uuid3(NAMESPACE_DNS, fileobj.name.encode('utf8'))
    filename =  '%s.%s' % (uuidstr, fileext)

    # Very poor test I know, but it works some of the way
    if fileext.lower() in ('jpg','jpeg','gif','png'):
        # The fact that we write the file once here and read it back into
        # the Billed object further down is *horrific* ... haven't had time
        # to find a more elegant solution yet though.
        destination = open('%s/%s' % (settings.MEDIA_ROOT, filename), 'wb+')

        for chunk in fileobj.chunks():
            destination.write(chunk)
        destination.close()

        b = Billed()
        b.filnavn = filename
        b.fil.save(
                filename,
                File(open('%s/%s' % (settings.MEDIA_ROOT, filename)))
                )
        b.save()

def upload(request):
    ''' Upload view that handles processing the POST message
        and send each individual file to handle_uploaded_file
    '''

    if request.method == 'POST':
        for afile in request.FILES.getlist('filelist'):
            handle_uploaded_file(afile)

    # Get the referer and send the user back there
    referer = request.META.get('HTTP_REFERER', '')
    return HttpResponseRedirect(referer)

def overview(request, stream=False):
    uploads = Billed.objects.all().order_by('-uploaded')

    c = {'object_list' : uploads}
    c.update(csrf(request))

    if stream:
        template = 'upload_list.html'
    else:
        template = 'overview.html'

    return render_to_response('upload/' + template, c)

def frontpage(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('frontpage.html', c)

# Login and logout related views
def login_view(request):
    ''' Login stuff
    '''

    c = {}
    c.update(csrf(request))

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    return render_to_response('login.html', c)

def logout_view(request):
    ''' Logout the user
    '''

    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/login')
