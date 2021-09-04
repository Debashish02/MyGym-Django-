from django.shortcuts import render

# Create your views here.
def gym(request):
    return render(request, "gym/main.html")

def workout(request):
    return render(request, "templates/index.html")