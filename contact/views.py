from django.shortcuts import render
from products.models import Product


def contact(request):
    """ A view to return the index page """

    return render(request, 'contact/contact.html')