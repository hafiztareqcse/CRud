from django.shortcuts import render
from .models import *
from . import forms

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'homepage': 'Musician List', 'musician': musician_list}
    return render(request, 'index.html', context=diction)

def form(request):
    new_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {'test_form': new_form, 'heading':'Add New Musician'}        
    return render(request, 'form.html', context=diction)