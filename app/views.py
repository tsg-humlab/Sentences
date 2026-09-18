"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'This project was conducted by',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def project1a(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Analysis.html',
        {
            'title':'Analysis file',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'intro':'Introduction',
            'graphs':'Graphs',
            'context':'Context',
            'pdf':'Link to PDF article',   
        }
    )

def project1b(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Analysis_comb.html',
        {
            'title':'Pros_cons',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'intro':'Introduction',
            'graphs':'Graphs',
            'context':'Context',
            'pdf':'Link to PDF article',   
        }
    )


def project1(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
         request,
         'app/project1.html',
         {
             'title':'Agent Based Modelling',
             'message':'Your application description page.',
             'year':datetime.now().year,
             'intro':'Introduction',
             'graphs':'Graphs',
             'context':'Context',
             'pdf':'Link to PDF article',      


         }
     )

def project2(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/project2.html',
        {
            'title':'What 55,000 tweets tell us about how the Dutch talk about cancer screening',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'intro':'Introduction',
            'graphs':'Graphs',
            'context':'Context',
            'pdf':'Link to PDF article',        

        }
    )

def project3(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/project3.html',
        {
            'title':'What people really say about cancer screening online: a look inside a Dutch discussion forum',
            'message':'',
            'year':datetime.now().year,
            'intro':'Introduction',
            'graphs':'Graphs',
            'context':'Context',
            'pdf':'Link to PDF article',   
        }
    )

def project4(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/project4.html',
        {
            'title':'Cancer screening in the Dutch news: a "necessary evil" that!s worth it',
            'message':'',
            'year':datetime.now().year,
            'intro':'Introduction',
            'graphs':'Graphs',
            'context':'Context',
            'pdf':'Link to PDF article',   
        }
    )