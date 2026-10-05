from django.db import models

from django.db import models

class Event(models.Model):
    class Category(models.TextChoices):
        EDUCATION = 'education', 'Education'
        TECHNOLOGY = 'technology', 'Technology'
        SPORT = 'sport', 'Sport'
        ENTERTAINMENT = 'entertainment', 'Entertainment'
        OTHER = 'other', 'Other'

    class Status(models.TextChoices):
        UPCOMING = 'upcoming', 'Upcoming'
        ONGOING = 'ongoing', 'Ongoing'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER
    )
    location = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.UPCOMING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title