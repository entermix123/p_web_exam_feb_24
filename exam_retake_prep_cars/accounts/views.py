from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from exam_retake_prep_cars.accounts.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from exam_retake_prep_cars.accounts.models import Profile
from exam_retake_prep_cars.cars.models import Car
from exam_retake_prep_cars.web.views import get_profile


def create_profile_page(request):
    form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, template_name='profile/profile-create.html', context=context)


def edit_profile_page(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def user_details_view(request):
    current_user = get_profile()
    cars = Car.objects.filter(owner=current_user)
    total_cars_price = sum([x.price for x in cars])

    context = {
        'total_cars_price': total_cars_price,
        'profile': current_user,
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile_page(request):
    profile = get_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
