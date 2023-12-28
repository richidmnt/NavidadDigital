from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')
def villancicos(request):
    return render(request,'villancicos.html')
def recetas(request):
    return render(request,'recetas.html')
def variedades(request):
    return render(request,'variedades.html')
def gramola(request):
    return render(request,'gramola.html')
def sms(request):
    return render(request,'sms.html')
def  belen(request):
    return render(request,'belenes.html')
def encales(request):
    return render(request,'enlaces.html')
def villancico1(request):
    return render(request,'belenPastores.html')
def villancico2(request):
    return render(request,'villancico2.html')
def villancico3(request):
    return render(request,'villancico3.html')
def villancico4(request):
    return render(request,'villancico4.html')
def villancico5(request):
    return render(request,'villancico5.html')
def receta1(request):
    return render(request,'receta1.html')
def receta2(request):
    return render(request,'receta2.html')