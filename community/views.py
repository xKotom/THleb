from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import User, ProfileTag


@login_required
def people_list(request):
    mode = request.GET.get('mode', 'friends')
    user = request.user
    user_tags = list(user.tags.values_list('tag', flat=True))

    people = User.objects.exclude(id=user.id)

    gender = request.GET.get('gender')
    if gender:
        # filter by bio containing gender keyword (simplified)
        pass

    if user_tags:
        people = people.filter(tags__tag__in=user_tags).annotate(
            match_count=Count('tags', filter=Q(tags__tag__in=user_tags))
        ).order_by('-match_count')
    else:
        people = people.order_by('?')

    return render(request, 'community/people_list.html', {
        'people': people.distinct()[:20],
        'mode': mode,
    })


@login_required
def person_detail(request, user_id):
    person = User.objects.get(id=user_id)
    return render(request, 'community/person_detail.html', {
        'person': person,
    })
