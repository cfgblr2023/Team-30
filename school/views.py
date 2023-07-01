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

from django.views import View
from django.http import JsonResponse
from .models import imageinsert
from .get_category import get_result
import io
from PIL import Image
import matplotlib.pyplot as plt

class ImageUploadView(View):
    def post(self, request):
        name = request.POST.get('name')
        image_file = request.FILES.get('image')
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
            my_model = imageinsert.objects.create(image=image_file, name=name)
            in_memory_uploaded_file.seek(0)
            image_data = in_memory_uploaded_file.read()
            pil_image = Image.open(io.BytesIO(image_data))
            mpimg = plt.imread(pil_image)
            return redirect('image_upload_success')
    return render(request, 'school/Contribute.html')

def image_upload_success_view(request):
    return render(request, 'school/image_upload_success.html')