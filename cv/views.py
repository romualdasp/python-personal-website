from django.shortcuts import render, redirect, get_object_or_404
from cv.models import Skill
from django.http import HttpResponse

# Create your views here.

def cv_preview(request):
    skills = Skill.objects.all()
    return render(request, 'cv/cv_preview.html', {'skills': skills})

def skill_new(request):
    if request.method == 'POST':
        Skill.objects.create(text=request.POST['skill_text'])
    return redirect('cv_preview')

def skill_remove(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('cv_preview')
