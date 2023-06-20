from django.shortcuts import render
from .models import Entry

def guestbook(request):
    if request.method == 'POST':
        author = request.POST['author']
        message = request.POST['message']
        entry = Entry(author=author, message=message)
        entry.save()

    entries = Entry.objects.all().order_by('-created_at')

    return render(request, 'guestbook.html', {'entries': entries})
