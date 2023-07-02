from django import forms
from django.contrib.auth.models import User
from . import models
from .models import imageinsert

#for order
class OrderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    image=forms.ImageField()
    class Meta:
        model = imageinsert
        fields = ['name', 'image','address']

# #for admin
# class AdminSigupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']

# #for frenchise



# #for student related form
# class StudentUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']







# #for Attendance related form
# presence_choices=(('Present','Present'),('Absent','Absent'))
# class AttendanceForm(forms.Form):
#     present_status=forms.ChoiceField( choices=presence_choices)
#     date=forms.DateField()

# class AskDateForm(forms.Form):
#     date=forms.DateField()








# #for contact us page
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



# class FormSettings(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(FormSettings, self).__init__(*args, **kwargs)
#         # Here make some changes such as:
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-control'

