from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def watch(request):
    return render(request, 'watch.html')

def learn(request):
    return render(request, 'learn.html')

def see(request):
    return render(request, 'see.html')

def about(request):
    return render(request, 'about.html')

