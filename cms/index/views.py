from django.shortcuts import render


def index(request):
    contex = {"title": "Главная страница"}
    return render(request, "default-pages/index.html", contex)
