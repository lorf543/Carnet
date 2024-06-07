from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('add/',views.agent_add, name='agent_add'),
    path('update/<int:agent_id>/',views.agent_update, name='agent_update'),
    path('detail/<int:agent_id>/',views.agent_detail, name='agent_detail'),
    path('scan_qr/',views.scan_qr, name='scan_qr'),
    path('validate/', views.validate, name='validate'),
]

htmx_urlpatterns = [
    path('check_id/',views.check_id,name='check_id'),
]

urlpatterns += htmx_urlpatterns
