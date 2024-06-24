from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

EMPLOYEE_STATUS = (
    ('Activo','Activo'),
    ('Inactivo','Inactivo')
)

from .models import Agent

def idVal(value):
    patron = r'^[0-9]*$' 
    if not re.match(patron, value):
        raise forms.ValidationError('Solo numeros permitidos')

class AgentForm(forms.ModelForm):

    identification = forms.CharField(
        min_length= 11,
        max_length=11,
        label='Identificacion',
        validators=[idVal],
        error_messages={
            'required': 'Este campo es requerido',
        },
        widget=forms.TextInput(
            attrs={
                'hx-post':'/check_id/',
                'hx-swap':'outerhtml',
                'hx-triger':'keyup delay:1s',
                'hx-target':'#id_error',
                'x-data x-mask': '(999)-999-9999',
            }   
    ))

    profile_picture = forms.FileField(
        label="foto de perfil",
        
        widget=forms.ClearableFileInput(
            attrs={
                'accept':'image/png, image/jpeg',
            }
        ),
        error_messages={
            'required': 'Este campo es requerido',
        }
    )

    first_name = forms.CharField(
        label='Nombres',
        error_messages={
            'required': 'Este campo es requerido',
        },
        validators=[
        RegexValidator('^[a-zA-ZÀ-ÿ\s]*$',
        message='Sole letras permitidas')
        ],
    )
    last_name = forms.CharField(
        label='Apellido',
        error_messages={
            'required': 'Este campo es requerido',
        },
        validators=[
        RegexValidator('^[a-zA-ZÀ-ÿ\s]*$',
        message='Sole letras permitidas')
        ],
    )

    rank = forms.CharField(
        label='Rango',
        error_messages={
            'required': 'Este campo es requerido',
        }
    )
    employee_status  = forms.ChoiceField(
        choices=EMPLOYEE_STATUS,
        label='Departamento',
        error_messages={
            'required': 'Este campo es requerido',
        }
    )
    height  = forms.CharField(
        label='Altura',
        max_length=3,
        error_messages={
            'required': 'Este campo es requerido',
        },
        validators = [RegexValidator('^\d+(\.\d+)?$',
        message='Ingreso un numero valido (e.g., 5 or 5.5).',
        code='invalid_input')],
        widget=forms.TextInput(attrs={'type':'number'})
    )
    eyes  = forms.CharField(
        label='Color de Ojos',
        error_messages={
            'required': 'Este campo es requerido',
        },    
    )
    skin  = forms.CharField(
        label='Color de Piel',
        error_messages={
            'required': 'Este campo es requerido',
        },
    )
    weight  = forms.CharField(
        label='Peso',
        max_length=3,
        validators = [RegexValidator('^[0-9]*$',
        message='Only Numbers Allowed')],
        error_messages={
            'required': 'Este campo es requerido',
        },
        widget=forms.TextInput(attrs={'type':'number'})
    )
    blood_type  = forms.CharField(
        label='Tipo de sangre',
        max_length=2,
        error_messages={
            'required': 'Este campo es requerido',
        },
    )
    carnet_status  = forms.CharField(
        required=False,
        error_messages={
            'required': 'Este campo es requerido',
        },
        label='Estado de Carnet',
    )
    

    class Meta:
        model = Agent
        fields = (
            'profile_picture','first_name','last_name','rank','employee_status',
            'carnet_status','identification','height','eyes','skin','weight','blood_type'
            )

