from django.shortcuts import render
from django.http  import HttpResponse
from django.http  import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import Use
import random

# Create your views here.


