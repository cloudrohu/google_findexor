from django.shortcuts import render

# Create your views here.


def index(request):
    #category = categoryTree(0,'',currentlang)

    return render(request, 'index.html',)
