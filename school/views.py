from django.shortcuts import render,redirect,reverse,get_object_or_404
from . import models
from django.views.static import serve
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.core.mail import send_mail
from .forms import OrderForm
from school import models
from schoolmanagement import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from django.views import View
from django.http import JsonResponse
from .models import imageinsert
from .get_category import get_result
import io
from PIL import Image
import matplotlib.pyplot as plt

def home(request):
    return render(request, "school/index.html")

def contactus(request):
    return render(request, "school/ContactUs.html")

def category(request):
    return render(request, "school/Categories.html")

class ImageUploadView(View):
    def post(self, request):
        name = request.POST.get('name')
        image_file = request.FILES.get('image')
        address = request.POST.get('address')
        if image_file:
            my_model = imageinsert.objects.create(image=image_file, name=name)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'No image file provided.'})

def serve_image(request, image_path):
    return serve(request, image_path, document_root=settings.MEDIA_ROOT)

def image_upload_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image_file = request.FILES.get('image')
        if image_file:
            # image_file.seek(0)
            # image_data = image_file.file.read()
            # pil_image = Image.open(io.BytesIO(image_data))
            # mpimg = plt.imread(pil_image)
            img = Image.open(image_file)
            np_image = np.array(img)
            res = get_result(np_image)
            my_model = imageinsert.objects.create(image=image_file, name=name,preditions=res)
            return render(request, 'school/UserGuidelines.html', {'name':name, "prediction": res})
    return render(request, 'school/UserGuidelines.html')

def image_upload_success_view(request):
    return render(request, 'school/image_upload_success.html')