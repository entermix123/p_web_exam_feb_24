from django.urls import path

from exam_retake_prep_cars.accounts.views import user_details_view, create_profile_page, \
    edit_profile_page, delete_profile_page

urlpatterns = (
    path('craete/', create_profile_page, name='create_profile'),
    path('details/', user_details_view, name='profile_details'),
    path('edit/', edit_profile_page, name='edit_profile'),
    path('delete/', delete_profile_page, name='delete_profile'),
)
