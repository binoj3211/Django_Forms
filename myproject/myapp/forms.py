from django import forms
from django.core.exceptions import ValidationError
from myapp.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ["name", "content"]
        # exclude = ["name"]

    def clean(self):

        """

        Raise `ValidationError` if user didn't provide both name and email.

        """

        cleaned_data = super().clean()

        full_Name = cleaned_data.get("name")

        email = cleaned_data.get("email")

        age = cleaned_data.get("age")

       

        if age <18:

             raise ValidationError("Must be greater than 18.")



        if not full_Name and not email:

            raise ValidationError("Please provide name or email.")

       

        return cleaned_data
