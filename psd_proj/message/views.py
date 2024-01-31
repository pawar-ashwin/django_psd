from django.http import HttpResponse
def homeMessageView(request):
    return HttpResponse('<h1 style="color:blue;">Hello, World!</h1>')