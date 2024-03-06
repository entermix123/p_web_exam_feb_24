from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_retake_prep_cars.accounts.models import Profile
from exam_retake_prep_cars.cars.validators import validate_car_year


class Car(models.Model):

    class CarChoices(models.TextChoices):
        # "Rally", "Open-wheel", "Kart", "Drag" and "Other"
        RALLY = "Rally",
        OPEN_WHEEL = "Open-wheel",
        KART = "Kart",
        DRAG = "Drag",
        OTHER = "Other"

    MAX_LENGTH_CHOICE = 10
    MAX_LENGTH_MODEL = 15
    MIN_LENGTH_MODEL = 1
    MIN_PRICE_VALUE = 1.0

    type = models.CharField(
        max_length=MAX_LENGTH_CHOICE,
        choices=CarChoices.choices,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=[
            MinLengthValidator(MIN_LENGTH_MODEL),
        ],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=[
            validate_car_year,
        ],
        blank=False,
        null=False,
    )

    # TODO: placeholder - "https://..."
    image_url = models.URLField(
        unique=True,
        error_messages={'unique': "This image URL is already in use! Provide a new one."},
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE_VALUE),
        ],
        blank=False,
        null=False,
    )

    # TODO: set hidden field for car owner
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
