from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_retake_prep_cars.accounts.models import Profile
from exam_retake_prep_cars.cars.models import Car
from exam_retake_prep_cars.web.views import get_profile


class ProfileCreateView(views.CreateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password')
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('index')

    # Set placeholders in fields
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['password'].widget = forms.PasswordInput(
            # attrs={'placeholder': 'enter your password'},
        )

        return form


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile_details')

    # Set placeholders in fields
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['password'].widget = forms.PasswordInput(
            # attrs={'placeholder': 'enter your password'},
        )

        return form


class ProfileDetailView(views.DetailView):
    queryset = Profile.objects.all()
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch dynamic data based on the object being viewed
        cars = self.cars.all()
        total_price = sum(car.price for car in cars)  # Assuming get_additional_data fetches data based on the object
        context['total_price'] = total_price
        return context

    # get pk for current profile
    def get_object(self, queryset=None):
        return get_profile()

    # context with dynamic data - overwrite det_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_price'] = self.get_total_price()  # set dynamic on refresh

        return context

    def get_total_price(self):
        return sum(car.price for car in self.cars)

    extra_context = {
        'cars': cars,
        'total_price': total_price,
    }


def user_details_view(request):
    # current_user = get_profile()
    current_user = Profile.objects.first()
    cars = Car.objects.filter(owner=current_user)
    total_cars_price = sum([x.price for x in cars])

    context = {
        'total_cars_price': total_cars_price,
        'profile': current_user,
    }

    return render(request, 'profile/profile-details.html', context)


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')
