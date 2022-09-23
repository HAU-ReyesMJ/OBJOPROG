from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home_view(request,  *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    context = { 'obj': request.user }
    #return HttpResponse("<h1>Hello World</h1>")
    if request.user.is_authenticated:
        return render(request, "home.html", context)
    return redirect('/login')

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me Page",
        "my_number": 123,
        "my_list": [1, 2, 3, 4],
    }
    return render(request, "about.html", my_context)