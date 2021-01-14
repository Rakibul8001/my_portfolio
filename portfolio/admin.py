from django.contrib import admin
from .models import Resume,About,Experience, Education,Project,Skill
# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name','title','cv_file']
    class Meta:
        model = Resume

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title','company_name','start_date','end_date']
    class Meta:
        model = Experience

class EducationAdmin(admin.ModelAdmin):
    list_display = ['institute_name','degree','start_date','end_date']
    class Meta:
        model = Education

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    class Meta:
        model = Project

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
    class Meta:
        model = Skill

class AboutAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = About

admin.site.register(Resume,ResumeAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(About,AboutAdmin)