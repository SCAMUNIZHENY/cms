from django.shortcuts import render


def console(request):
    contex = {"title": "Консоль"}
    return render(request, "index/index.html", contex)
