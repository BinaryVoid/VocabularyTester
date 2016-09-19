try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import vocabForm
from .models import vocabulary
# Create your views here.
# 9977282633

def word_name(request):
	vocab_obj=

# 9753611576