from django.shortcuts import render


def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def index(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
