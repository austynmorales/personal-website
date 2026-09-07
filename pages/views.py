from django.shortcuts import render

def home(request):
    items = [
        {'name': 'Learn Django', 'completed': True},
        {'name': 'Build a personal website', 'completed': True},
        {'name': 'Learn Python', 'completed': False},
        {'name': 'Create Portfolio', 'completed': True},
        {'name': 'Finish Web Development Course', 'completed': False},
    ]

    return render(request, 'home.html', {'items': items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
