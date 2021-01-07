from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import ContactForm

destinations = ['Solo', 'Road', 'Tropical', 'Safari']

def home(request):
    return render(request, 'home.html', {})

def discover(request):
    return render(request, 'discover.html', {
        'destinations': destinations
    })

def discover_detail(request, destination):
    if destination not in destinations:
        raise Http404('Destination not found')
    return render(request, 'discover_detail.html', {
        'destination': destination
    })

def blog(request):
    return render(request, 'blog.html', {})

def gallery(request):
    topics = ['beach', 'travel', 'nature', 'travel', 'water', 'building', 'trees', 'cruise', 'beaches', 'traveling', 'bridge', 'boat']
    return render(request, 'gallery.html', {
        'topics': topics
    })

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    return render(request,'contact.html',{'form':form})