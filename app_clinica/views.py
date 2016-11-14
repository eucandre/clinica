from django.shortcuts import render
from django.shortcuts import *
def inicia(request):
    return render_to_response("base.html")
