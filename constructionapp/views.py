from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')