from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import RegisterForm, ProfileForm, TagForm
from .models import ProfileTag, Event


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    tag_form = TagForm(initial={
        'tags': ', '.join(t.tag for t in request.user.tags.all())
    })

    events = Event.objects.filter(date__gte=timezone.now())
    registered_events = request.user.event_registrations.values_list('event_id', flat=True)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'tag_form': tag_form,
        'purchases': request.user.purchases.all()[:10],
        'events': events,
        'registered_events': list(registered_events),
    })


@login_required
def save_tags(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tags_str = form.cleaned_data['tags']
            tags = [t.strip() for t in tags_str.split(',') if t.strip()]
            request.user.tags.all().delete()
            for tag in tags:
                ProfileTag.objects.create(user=request.user, tag=tag)
    return redirect('profile')


@login_required
def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    request.user.event_registrations.get_or_create(event=event)
    return redirect('profile')
