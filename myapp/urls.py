from django.contrib import admin
from django.urls import path, include
from . import views
from practice import views as prac_views

urlpatterns = [
    path('myapp/', views.home, name='home'),
    path('myapp/about/', views.about, name='about'),
    path('myapp/guestbook/', views.guestbook, name='guestbook'),
    path('myapp/delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('myapp/edit/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('myapp/admin/', admin.site.urls),
    path('practice/', prac_views.index),

]