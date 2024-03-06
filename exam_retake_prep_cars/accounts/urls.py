from django.urls import path

from exam_retake_prep_cars.accounts.views import ProfileCreateView, ProfileUpdateView, \
    ProfileDeleteView, user_details_view

urlpatterns = (
    path('craete/', ProfileCreateView.as_view(), name='create_profile'),
    path('details/', user_details_view, name='profile_details'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete_profile'),
)
