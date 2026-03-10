from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback


@login_required
def feedback_home(request):
    return render(request, 'feedback/home.html')


@login_required
def complaint(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.type = 'complaint'
            fb.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/form.html', {
        'form': form,
        'title': 'Хочу пожаловаться',
    })


@login_required
def praise(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.type = 'praise'
            fb.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/form.html', {
        'form': form,
        'title': 'Расскажу о хорошем',
    })


@login_required
def thanks(request):
    return render(request, 'feedback/thanks.html')
