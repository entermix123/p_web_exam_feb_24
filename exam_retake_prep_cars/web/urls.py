from django.urls import path

from exam_retake_prep_cars.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
