from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'placeholder': 'Enter title or location'})
    )

CATEGORY_CHOICES = [
    ("education", "Education"),
    ("technology", "Technology"),
    ("sport", "Sports"),
    ("entertainment", "Entertainment"),
    ("other", "Other"),
]

STATUS_CHOICES = [
    ("upcoming", "Upcoming"),
    ("ongoing", "Ongoing"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
]


def censored(value):
    if "nigga" in value or "test" in value in value or "spam" in value in value or "virus" in value:
        raise ValidationError("Such word is forbidden")

class EventForm(forms.Form):
    title = forms.CharField(
        label="Title",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Event title",
        }),
        validators=[censored],
    )
    description = forms.CharField(
        label="Description",
        min_length=20,
        max_length=500,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "What is this event about?",
        }),
        validators=[censored],
    )
    category = forms.ChoiceField(
        label="Category",
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        validators=[censored],
    )
    location = forms.CharField(
        label="Location",
        min_length=10,
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Venue, room or address",
        }),
        validators=[censored],
    )
    status = forms.ChoiceField(
        label="Status",
        choices=STATUS_CHOICES,
        initial="upcoming",
        widget=forms.Select(attrs={"class": "form-select"}),
        validators=[censored],
    )
