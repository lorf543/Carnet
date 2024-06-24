from django.contrib import admin
from .models import Agent
from .forms import AgentForm
from django.utils.html import format_html

# Register your models here.


class AgentAdmin(admin.ModelAdmin):
   form = AgentForm
   fieldsets = [
        ('Informacion Personal',{
           'fields':['profile_picture',('first_name','last_name'),('rank','id_carnet','employee_status','carnet_status'),'identification']
        }),
        ('Informacion Carnet',{
           'fields':['num_print',('created','updated','added_by','updated_by')]
        }),
        ('Informacion fisica',{
           'fields':[('eyes','skin'),('height','weight'),'blood_type']
        })
        
   ]

   readonly_fields = ['num_print','created','updated','added_by','updated_by','rank']


admin.site.register(Agent,AgentAdmin)


    
