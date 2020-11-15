from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .services import visual_recognition
from .models import Image, ImageLabel
import json
from django.conf import settings
import os


def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_object = form.instance

            # Call the Visual Recognition API to get image labels
            recognition_results = visual_recognition.classify(
                url=image_object.image.url
            ).get_result()

            # Save each of them as an ImageLabel object to the database
            for result in recognition_results["images"][0]["classifiers"][0]["classes"]:
                image_label = ImageLabel(
                    image=image_object, label=result["class"], score=result["score"]
                )
                image_label.save()

            # Get the list of labels, in descending order of scores
            image_labels = ImageLabel.objects.filter(image=image_object).order_by(
                "-score"
            )
            return render(
                request,
                "index.html",
                {
                    "form": form,
                    "image_object": image_object,
                    "image_labels": image_labels,
                },
            )
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})


def history(request):
    image_objects = Image.objects.all().order_by("-uploaded_at")
    return render(request, "history.html", {"image_objects": image_objects})
