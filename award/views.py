from django.shortcuts import render
from django.http  import HttpResponse
from django.http  import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import Use
import random
from .models import Posts, UserProfile,Ratings
from .forms import  UpdateUserForm, UpdateUserProfileForm,UserSignupForm,PostsForm,RatingsForm

# Create your views here.

def index(request):
    current_user = request.user
    if request.method == "POST":
        form = PostsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = PostsForm()
    
    try:
        posts = Posts.objects.all()
        posts = posts[::-1]
        post_index = random.randint(0, len(posts)-1)
        random_post = posts[post_index]
        print(random_post.photo)
    except Posts.DoesNotExist:
        posts = None
    return render(request, 'all-awards/home.html',{'form':form,'current_user':current_user,'random_post': random_post,'posts':posts})

