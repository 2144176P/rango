from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # NB The key 'boldmessage' is the same as {{ boldmessage }} in the HTML template
    context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to client.
    # We make use of the shortcut function
    # NB the first parameter is the template we wish to use i.e rango/index.html
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    return HttpResponse("Rango says here is the about page.  <a href='/rango/'>Index</a>")