from django.shortcuts import render

# Create your views here.

def createprofile(request):
    return render(request, 'profileupload/userupload.html')