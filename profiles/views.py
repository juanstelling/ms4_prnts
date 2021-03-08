from django.shortcuts import render


def profile(request):
    """Shows the user's profile/account"""

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
