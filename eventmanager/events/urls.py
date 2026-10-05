from tkinter.font import names

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.events_page,name='events'),
    path('<int:event_id>/',views.event_page,name='event_detail'),
    path('delete/<int:event_id>/',views.delete_page,name='delete_event'),
    path('create/',views.create_page,name='create_event')
]
