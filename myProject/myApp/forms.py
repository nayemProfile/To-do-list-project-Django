from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserCreateForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = UserCreationForm.Meta.fields + ('display_name', 'email','user_type', 'password1', 'password2')
        
        
class UserSigninForm(AuthenticationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'password']
        
        
class TaskCatagorizForm(forms.ModelForm):
    class Meta:
        model = Task_Catagorze
        fields = ['catagori_title']
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = ('__all__')
        exclude = ['task_status']
        labels = {
            'task_title':'Your Task Title',
            'task_descreption':'Your Task Description',
            'task_categorize':'Your Task Categorize',
            'task_priroty':'Your Task priroty',
        }
      
        
class TaskPryrotyForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields =[ 'task_priroty', 'task_categorize',]
        labels = {
            'task_categorize':'Your Task Categorize',
            'task_priroty':'Your Task priroty',
        }
        