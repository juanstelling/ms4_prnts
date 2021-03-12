from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator

from newsletter.forms import EmailSubscribeForm


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    form = EmailSubscribeForm()

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'home/index.html', context)
