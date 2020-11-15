from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .visual_recognition import visual_recognition
from .models import Image, ImageLabel
import json

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_object = form.instance
            return render(request, "index.html", {
                "form": form, 
                "image_object": image_object
            })
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})
