from django.shortcuts import render
from django import forms 

class IncidentReport(forms.Form):
    reporter = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

    date_incident = forms.CharField(max_length=20)
    date_reported = forms.CharField(max_length=20)
    date_update = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)


# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def add_new(request):
    context = {
    }

    return render(request, 'pages/about.html', context)
