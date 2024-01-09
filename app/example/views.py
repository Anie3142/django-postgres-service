from django.http import HttpResponse
import datetime

def homepage(request):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content = f"<h1>Study Group App</h1><p>Current Date and Time: {current_time}</p>"
    return HttpResponse(content)

def health_check(request):
    return HttpResponse("OK")
