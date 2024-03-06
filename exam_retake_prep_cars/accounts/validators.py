from django.core.exceptions import ValidationError


def validate_username(username):
    is_valid = any(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")
