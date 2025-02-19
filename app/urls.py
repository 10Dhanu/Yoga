from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hatha_yoga/', views.hatha_yoga, name='hatha_yoga'),
    path('ashtanga_yoga/', views.ashtanga_yoga, name='ashtanga_yoga'),
    path('face_yoga/', views.face_yoga, name='face_yoga'),
    path('parent_child_yoga/', views.parent_child_yoga, name='parent_child_yoga'),
    path('meditation_detox/', views.meditation_detox, name='meditation_detox'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
