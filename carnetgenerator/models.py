from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

import random

from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    profile_picture = models.FileField(upload_to='profile_picture', max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    id_carnet = models.CharField(max_length=50, null=True, blank = True)
    employee_status = models.CharField(max_length=50)
    carnet_status = models.CharField(max_length=50, null=True, blank = True)
    qr_code = models.ImageField(upload_to='qr_code', null=True, blank = True)
    
    #______________personal_info_______________________
    identification = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    eyes = models.CharField(max_length=50)
    skin = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=50)

    #______________carnet_info_____________
    num_print = models.IntegerField(null=True, blank = True)
    created = models.DateField(auto_now_add=True, null=True, blank = True)
    updated = models.DateField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_by', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update_by',null=True, blank = True)

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        
        if not self.id_carnet:
            while True:
                random_code = random.randint(10000000, 99999999)
                if not Agent.objects.filter(id_carnet=random_code).exists():
                    self.id_carnet = random_code
                break            

        #if self._state.adding:
            qrcode_image =qrcode.make(self.id_carnet)
            canvas = Image.new('RGB', (290,290), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_image)
            fname = f'qr_code={self.id_carnet}.png'
            buffer = BytesIO()
            canvas.save(buffer,'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()

            super().save(*args, **kwargs)



@receiver(post_save, sender=Agent)
def set_id_carnet(sender, instance, *args, **kwargs):
    if instance._state.adding:

    
        post_save.connect(set_id_carnet, sender=Agent)