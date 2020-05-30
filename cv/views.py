from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cv_preview(request):
    return render(request, 'cv/cv_preview.html', {
        'skill_text_var': request.POST.get('skill_text', ''),
    })
