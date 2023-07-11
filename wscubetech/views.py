from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        'title': 'Home Page',
        'content': 'This is our content',
        'clist': ['PHP', 'Java', 'Django'],
        'student': [
            {'name': 'Abhijeet', 'phone': "901901"},
            {'name': 'abhi', 'phone': "9011901"}
        ],
        'numbers': [10, 20, 20, 40]
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse(
        "<h1>Welcome to wscubetech</h1>")


def Course(request, courseId):
    return HttpResponse(courseId)
