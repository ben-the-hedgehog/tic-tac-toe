from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello, World!")

def test(request):
    return HttpResponse(
    "<h1>Test</h1>"
    )
