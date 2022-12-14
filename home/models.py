from django.db import models
from django.contrib.auth.models import User
import uuid
import os
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Folders(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
#     access_by = ArrayField(
#        models.CharField(blank=True, max_length=150,default=""),default="",
#        blank=True,
#    )
    access_by =models.CharField(blank=True, max_length=150,default="")
    

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folders.uid), filename)

class Files(models.Model):
    folders = models.ForeignKey(Folders, on_delete= models.CASCADE, related_name='files')
    created_at = models.DateField(auto_now=True)
    file = models.FileField( upload_to=get_upload_path)
