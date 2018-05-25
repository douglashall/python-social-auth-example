from django.shortcuts import render

from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

