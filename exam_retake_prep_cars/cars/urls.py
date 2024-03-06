from django.urls import path

from exam_retake_prep_cars.cars.views import CatalogueView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView

urlpatterns = (
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('create/', CarCreateView.as_view(), name='create_car'),
    path('<int:pk>/details/', CarDetailView.as_view(), name='car_details'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='edit_car'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car'),
)

