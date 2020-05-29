from django.shortcuts import render

# Create your views here.

def cv_preview(request):
    return render(request, 'cv/cv_preview.html')
