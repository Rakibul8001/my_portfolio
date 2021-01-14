from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Resume,About,Experience,Education,Project,Skill

# Create your views here.
class HomeView(ListView):
    model = Experience
    template_name = "portfolio/index.html"


    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['projects'] = Project.objects.all()
        context['skills'] = Skill.objects.all()
        context['abouts'] = About.objects.all()
        return context