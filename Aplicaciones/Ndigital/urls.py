from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('villancicos/',views.villancicos,name="villancicos"),
    path('recetas/',views.recetas,name="recetas"),
    path('variedades/',views.variedades,name="variedades"),
    path('gramola/',views.gramola,name="gramola"),
    path('sms/',views.sms,name="sms"),
    path('belen/',views.belen,name="belen"),
    path('enlaces/',views.encales,name="enlaces"),
    path('belenPastores/',views.villancico1,name="villancico1"),
    path('villancico2/',views.villancico2,name="villancico2"),
    path('villancico3/',views.villancico3,name="villancico3"),
    path('villancico4/',views.villancico4,name="villancico4"),
    path('villancico5/',views.villancico5,name="villancico5"),
    path('receta1/',views.receta1,name="receta1"),
    path('receta2/',views.receta2,name="receta2")
]