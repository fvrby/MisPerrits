from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/login', views.login_page, name='login_page'),
    #Perritos
    path('index/', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('adopta/', views.adopta, name='adopta'),
    path('perritos_disponibles/', views.perritos_disponibles, name='perritos_disponibles'),
    path('perritos_adoptados/', views.perritos_adoptados, name='perritos_adoptados'),
    path('perritos_rescatados/', views.perritos_rescatados, name='perritos_rescatados'),
    path('detalle_perro/<int:pk>/', views.detalle_perro, name='detalle_perro'),
    path('detalle_perro/<int:pk>/adoptar', views.adoptar_perro, name='adoptar_perro'),
]
