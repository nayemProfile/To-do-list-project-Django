
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', signUp, name = 'signUp'),
    path('', singIn, name = 'singIn'),
    path('home', homePage, name = 'homePage'),
    path('signOut', signOut, name = 'signOut'),
    
    path('activate/<uid64>/<token>', activate,name='activate'), #email varification
    
    
    path('forget_pass', forget_pass,name='forget_pass'),   # forget password
    path('update_pass', update_pass,name='update_pass'), # forget password
    
    
    path('addTask', addTask, name = 'addTask'),
    path('viewTask', viewTask, name = 'viewTask'),
    path('editTask/<str:id>', editTask, name = 'editTask'),
    path('deleteTask/<str:id>', deleteTask, name = 'deleteTask'),
    path('taskStatus/<str:id>', taskStatus, name = 'taskStatus'),
    path('search/', search, name = 'search'),
    path('todayTask/', todayTask, name = 'todayTask'),
    
    
    path('addTaskCatagoriz', addTaskCatagoriz, name = 'addTaskCatagoriz'),
    path('editCatagoriz/<int:id>', editCatagoriz, name = 'editCatagoriz'),
    path('deleteCatagoriz/<str:id>', deleteCatagoriz, name = 'deleteCatagoriz'),
]
