from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):
    # images = Image.get_images()
    current_user = request.user

    title = 'Timeline'

    # user_info = Profile.objects.get(user=current_user.id)


    return render(request, 'index.html', {"title": title, "user": current_user })
