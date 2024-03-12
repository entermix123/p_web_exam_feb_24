from django.shortcuts import render

from exam_retake_prep_cars.accounts.models import Profile


def get_profile():  # check if profile is logged in
    return Profile.objects.first()


def index(request):
    current_profile = get_profile()

    context = {
        "profile": current_profile,
    }

    return render(request, 'index.html', context)
