from django.shortcuts import render, redirect, get_object_or_404
from cv.models import Skill, Education, Achievement, Course
from .forms import SkillForm, EducationForm, AchievementForm, CourseForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def cv_preview(request):
    return render(request, 'cv/cv_preview.html', {
        'skills': Skill.objects.all(),
        'educations': Education.objects.all(),
        'achievements': Achievement.objects.all(),
        'courses': Course.objects.all(),
    })

@login_required
def skill_new(request):
    return cv_new(request, SkillForm)

@login_required
def skill_remove(request, pk):
    return cv_remove(request, Skill, pk)

@login_required
def education_new(request):
    return cv_new(request, EducationForm)

@login_required
def education_remove(request, pk):
    return cv_remove(request, Education, pk)

@login_required
def achievement_new(request):
    return cv_new(request, AchievementForm)

@login_required
def achievement_remove(request, pk):
    return cv_remove(request, Achievement, pk)

@login_required
def course_new(request):
    return cv_new(request, CourseForm)

@login_required
def course_remove(request, pk):
    return cv_remove(request, Course, pk)

def cv_new(request, _ModelForm):
    if request.method == 'POST':
        form = _ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_preview')
    else:
        form = _ModelForm()
    return render(request, 'cv/cv_new.html', {'form': form})

def cv_remove(request, _Model, pk):
    instance = get_object_or_404(_Model, pk=pk)
    instance.delete()
    return redirect('cv_preview')
