from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Neighborhood,Post,Business,Profile
from .forms import NeighborhoodForm,PostMessageForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'Timeline'

    hoods = Neighborhood.get_neighborhoods

    return render(request, 'index.html', {"title": title, "user": current_user, "hoods":hoods })
def view_neighborhoods(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'Timeline'

    hoods = Neighborhood.get_neighborhoods

    return render(request, 'estates.html', {"title": title, "user": current_user, "hoods":hoods })



@login_required(login_url='/accounts/login')
def create_hood(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect(index)

    else:
        form = NeighborhoodForm()
    return render(request, 'new-hood.html', {"form":form})



@login_required(login_url='/accounts/login')
def hood_details(request, hood_id):
    '''
    View function to view details of a hood
    '''
    details = Neighborhood.get_specific_hood(hood_id)



    return render(request, 'hood-details.html',{"details":details})


@login_required(login_url='/accounts/login')
def post_message(request):
    '''
    View function to post a message
    '''
    current_user = request.user

    if request.method == 'POST':
        form = PostMessageForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.profile = current_user.id
            post.save()
            return redirect(index)

    else:
        form = PostMessageForm()
    return render(request, 'new-message.html', {"form":form})


@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create a profile
    '''
