from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_retake_prep_cars.accounts.validators import validate_username


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 3
    MIN_AGE_VALUE = 21
    MAX_PASSWORD_LENGTH = 20
    MAX_LENGTH_FIRST_NAME = 25
    MAX_LENGTH_LAST_NAME = 25

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_USERNAME, message="Username must be at least 3 chars long!"),
            validate_username,
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
          MinValueValidator(MIN_AGE_VALUE),
        ],
        help_text="Age requirement: 21 years and above.",
        blank=False,
        null=False,
    )

    # TODO: to appear as password on the form
    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def full_name(self):
        if self.first_name and self.last_name:
            full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name and not self.last_name:
            full_name = f"{self.first_name}"
        elif self.last_name and not self.first_name:
            full_name = f"{self.last_name}"
        else:
            full_name = ""
        return full_name
