from django.shortcuts import render, redirect
from cv.models import Skill
from django.http import HttpResponse

# Create your views here.

def cv_preview(request):
    if request.method == 'POST':
        Skill.objects.create(text=request.POST['skill_text'])
        return redirect('/cv/')

    skills = Skill.objects.all()
    return render(request, 'cv/cv_preview.html', {'skills': skills})

def clear_db(request):
    Skill.objects.all().delete()
    return redirect('/cv/')
