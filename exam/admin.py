from django.contrib import admin
from exam.models import Course, Result, Question

# Register your models here.
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Question)