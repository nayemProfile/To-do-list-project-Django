from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    USER=(
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    display_name = models.CharField(max_length = 50)
    user_type = models.CharField(choices = USER, max_length= 50)
    otp_token = models.CharField(max_length = 10, null= True) # only for forget password
    
    def __str__(self):
        return self.display_name
    
    
    
class Task_Catagorze(models.Model):
    catagori_title = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.catagori_title
    
    
class Task_Model(models.Model):
    Priroty = (
        ('Heigh', 'Heigh'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    task_title = models.CharField(max_length= 200)
    task_descreption = models.CharField(max_length= 500)
    task_categorize = models.ForeignKey(Task_Catagorze, on_delete = models.CASCADE, blank = True, null = True)
    task_priroty = models.CharField(choices = Priroty, max_length= 500, blank = True, null = True)
    task_date = models.DateTimeField(auto_now=True,  blank = True, null = True)
    task_status = models.BooleanField(default = False)
    
    def __str__(sefl):
        return sefl.task_title
    
    
    

    
