from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def message(request):
    if request.method == "POST":
        msg = request.POST["name"]
        print(msg)
