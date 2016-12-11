from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import UploadImageForm
from django.views.decorators.csrf import csrf_exempt
from models import verify_image
import json

def upload(request):
    form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})

def verify(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        data = {"success": True}
        # image = request.FILES['file']

        if form.is_valid():
            with open('/tmp/__img', 'wb+') as destination:
                for chunk in request.FILES['image'].chunks():
                    destination.write(chunk)

            faces = verify_image('/tmp/__img')
            num_faces = len(faces)
            if num_faces > 0:
                data['num_faces'] = num_faces
            else:
                data['success'] = False

            return JsonResponse(data)
        else:
            return render(request, 'upload.html', {'form': form})

    else:
        return redirect('/?redirected')
