from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {'movies': ['3 idiots', 'Jab we met', "Singham"], 'page':'Home'}
    return render(request, "movies/index.html", context)

def about(request):
    context = {'page': 'about'}
    return render(request, "movies/about.html", context)
