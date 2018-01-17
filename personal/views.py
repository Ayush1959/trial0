from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Email id : srihari.ayush@gmail.com'  '       Mobile no: 9633100673, 8891200673']})


# Create your views here.
