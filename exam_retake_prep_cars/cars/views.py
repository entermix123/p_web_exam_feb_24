from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from exam_retake_prep_cars.cars.models import Car
from exam_retake_prep_cars.mixins import ReadOnlyViewMixin
from exam_retake_prep_cars.web.views import get_profile


class CatalogueView(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context


class CarCreateView(views.CreateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    # Set placeholders in fields
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['image_url'].widget.attrs['placeholder'] = "https://..."

        return form

    # take owner from form
    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk

        return super().form_valid(form)


class CarDetailView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context


class CarUpdateView(views.UpdateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context


class CarDeleteView(ReadOnlyViewMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    # create form, because default views.DeleteView do not return deleted form
    form_class = modelform_factory(Car, fields=['type', 'model', 'year', 'image_url', 'price'])

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
