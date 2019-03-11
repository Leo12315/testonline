from django.shortcuts import render


# Create your views here.
def show_subject(request):
    return render(request, 'subject/subject.html')
