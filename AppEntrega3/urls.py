from django.urls import path
from AppEntrega3 import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio' ),
    path('registro/', views.registro, name='registro' ),
    path('ubicacion/', views.ubicacion, name='ubicacion' ),
    path('pelicula/', views.pelicula, name='pelicula' ),
    path('registroFormulario/', views.registro_Formulario, name='registroForm' ),
    path('ubicacionFormulario/', views.ubicacion_Formulario, name='ubicacionForm' ),
    path('peliculaFormulario/', views.pelicula_Formulario, name='peliculaForm' ),
    path('buscarInformacion/', views.busca_Informacion, name='buscarForm' ),

    path('buscar/', views.buscar, name='buscar'),
]


