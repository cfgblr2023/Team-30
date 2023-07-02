from django.contrib import admin
from django.urls import path , include
from school import views,models
from django.contrib.auth.views import LoginView,LogoutView
from school.views import image_upload_view, image_upload_success_view, home, category, contactus
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('Contribute', views.my_form_view, name='Contribute'),

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('/category', category, name='category'),
    path('/contactus', contactus, name='contactus'),
    path('upload/', image_upload_view, name='image_upload'),
    path('upload/success/', image_upload_success_view, name='image_upload_success'),
    # path('',views.home_view,name='home'),

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
