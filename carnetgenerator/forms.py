from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



from .models import Agent


class AgentForm(forms.ModelForm):

    identification = forms.CharField(
        min_length= 11,
        max_length=11,
        label='Identificacion',
        validators = [RegexValidator('^[0-9\-]*$',
        message='Only digits and hyphens are allowed.',
        code='invalid_input')],
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
    employee_status  = forms.CharField(
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
    )
    eyes  = forms.CharField(
        label='Ojos',
        error_messages={
            'required': 'Este campo es requerido',
        },    
    )
    skin  = forms.CharField(
        label='Piel',
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
        fields = "__all__"

