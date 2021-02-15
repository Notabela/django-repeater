from django.shortcuts import render

# Create your views here.
def repeat(request, name, times):
    return render(request, 'repeater/repeat.html', {
        'name': name,
        'times': range(times)
    })
