from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def neighborhood(request):
    return render(request, 'neighborhood/home.html')
