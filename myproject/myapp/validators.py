from django.core.exceptions import ValidationError


def gmail_validation(value):
    if value and not value.endswith("@gmail.com"):
        raise ValidationError("Provide a gmail account!")