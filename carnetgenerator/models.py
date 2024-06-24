from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import random

EMPLOYEE_STATUS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)

class Agent(models.Model):
    profile_picture = models.FileField(upload_to='profile_picture', max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    id_carnet = models.CharField(max_length=50, null=True, blank=True)
    employee_status = models.CharField(max_length=50, choices=EMPLOYEE_STATUS)
    carnet_status = models.CharField(max_length=50, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_code', null=True, blank=True)
    
    identification = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    eyes = models.CharField(max_length=50)
    skin = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=50)

    num_print = models.IntegerField(null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update_by', null=True, blank=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.id_carnet:
            # Encuentra el valor máximo actual de id_carnet en la base de datos
            max_id = Agent.objects.aggregate(models.Max('id_carnet'))['id_carnet__max']
            if max_id is None:
                # Si no hay ningún registro en la base de datos, empieza en 1
                new_id = 1
            else:
                # Incrementa el valor máximo en 1
                new_id = int(max_id) + 1

            # Formatea el nuevo id_carnet para que tenga 4 dígitos con ceros a la izquierda
            self.id_carnet = f"{new_id:04d}"


            qrcode_image = qrcode.make(self.id_carnet)
            canvas = Image.new('RGB', (290, 290), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_image)
            fname = f'qr_code={self.id_carnet}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()
        else:
            pass

        super().save(*args, **kwargs)
